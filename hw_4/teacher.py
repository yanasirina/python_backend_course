from user import User


class Teacher(User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._students = []

    def __str__(self):
        str_parent = super().__str__()
        return f'{str_parent} (учитель)'

    def add_student(self, student):
        self._students.append(student)

    def get_students(self):
        return self._students
