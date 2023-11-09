import os
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class FileException(Exception):
    pass


class Command:
    """Базовый класс для реализации команд для работы с файлом"""

    operation_name = 'Unnamed command'

    def __init__(self, file_name: str, file_manager: 'FileManager'):
        self.file_name = file_name
        self.file_manager = file_manager

    def execute(self):
        if not os.path.exists(self.file_name):
            raise FileException(f'Файла {self.file_name} не существует')

    def undo(self):
        pass


class ReadFileCommand(Command):
    """Команда для чтения файла"""

    operation_name = 'Read file'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_content = None

    def execute(self):
        super().execute()
        with open(self.file_name, 'r') as file:
            self.file_content = file.read()

    def undo(self):
        self.file_content = None


class WriteFileCommand(Command):
    """Команда для записи в файл"""

    operation_name = 'Write to file'

    def __init__(self, content, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = content
        self.previous_content = None

    def execute(self):
        super().execute()
        with open(self.file_name, 'r') as file:
            self.previous_content = file.read()
        with open(self.file_name, 'w') as file:
            file.write(self.content)

    def undo(self):
        if self.previous_content is not None:
            with open(self.file_name, 'w') as file:
                file.write(self.previous_content)


class DeleteFileCommand(Command):
    """Команда для удаления файла"""

    operation_name = 'Delete file'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_content = None

    def execute(self):
        super().execute()
        with open(self.file_name, 'r') as file:
            self.file_content = file.read()
        os.remove(self.file_name)

    def undo(self):
        if self.file_content is not None:
            with open(self.file_name, 'w') as file:
                file.write(self.file_content)


class ChangeFilePermissionsCommand(Command):
    """Команда для изменения прав доступа к файлу"""

    operation_name = 'Change file permission'

    def __init__(self, permissions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permissions = permissions
        self.previous_permissions = None

    def execute(self):
        super().execute()
        self.previous_permissions = os.stat(self.file_name).st_mode
        os.chmod(self.file_name, self.permissions)

    def undo(self):
        if self.previous_permissions is not None:
            os.chmod(self.file_name, self.previous_permissions)


class FileManager:
    """Менеджер файлов"""

    def __init__(self):
        self.commands = []

    def execute(self, command):
        command.execute()
        self.commands.append(command)
        logging.info(f'Execute command "{command.operation_name}", file: {command.file_name}')

    def undo(self):
        if self.commands:
            command = self.commands.pop()
            command.undo()
            logging.info(f'Undo command "{command.operation_name}", file: {command.file_name}')

    def execute_many(self, commands):
        for command in commands:
            self.execute(command)

    def undo_many(self, count):
        for _ in range(count):
            self.undo()


if __name__ == '__main__':
    file_manager = FileManager()
    file_name = 'example.txt'
    initial_file_content = 'Initial text'
    initial_file_permissions = 0o777

    # изначально в очереди нет задач
    assert len(file_manager.commands) == 0

    # создадим файл, с которым потом будет работать и добавим ему все разрешения
    with open(file_name, 'w') as file:
        file.write(initial_file_content)
    os.chmod(file_name, initial_file_permissions)

    # проверим, что команды корректно добавляются в очередь и удаляются из нее
    read_command = ReadFileCommand(file_name=file_name, file_manager=file_manager)
    file_manager.execute(read_command)
    assert len(file_manager.commands) == 1
    file_manager.execute(read_command)
    assert len(file_manager.commands) == 2
    file_manager.undo()
    assert len(file_manager.commands) == 1
    file_manager.undo()
    assert len(file_manager.commands) == 0
    file_manager.undo()
    assert len(file_manager.commands) == 0

    # проверим, что мы можем писать в файл и отменять операцию
    new_file_content = 'New content'
    write_command = WriteFileCommand(file_name=file_name, content=new_file_content, file_manager=file_manager)
    file_manager.execute(write_command)
    with open(file_name, 'r') as file:
        assert file.read().strip() == new_file_content
    file_manager.undo()
    with open(file_name, 'r') as file:
        assert file.read().strip() == initial_file_content

    # проверим функционал изменения прав
    new_permissions = 0o755
    change_permissions_command = ChangeFilePermissionsCommand(file_name=file_name, permissions=new_permissions, file_manager=file_manager)
    file_manager.execute(change_permissions_command)
    assert oct(os.stat(file_name).st_mode & 0o777) == oct(new_permissions)
    file_manager.undo()
    assert oct(os.stat(file_name).st_mode & 0o777) == oct(initial_file_permissions)

    # проверим функционал удаления файла
    delete_command = DeleteFileCommand(file_name, file_manager)
    file_manager.execute(delete_command)
    assert not os.path.exists(file_name)
    file_manager.undo()
    assert os.path.exists(file_name)

    # проверим выполнение нескольких команд
    commands = [read_command, write_command, change_permissions_command, delete_command]
    file_manager.execute_many(commands)
    assert len(file_manager.commands) == 4

    # проверим отмену сразу нескольких команд
    file_manager.undo_many(2)
    assert len(file_manager.commands) == 2

    # удалим созданный в начале файл
    file_manager.execute(delete_command)
