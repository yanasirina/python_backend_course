import bcrypt
from config import password_salt


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.__password = User.__encode_password(password)

    def __str__(self):
        return f'Пользователь: {self.username}'

    def __call__(self, password):
        if self.__is_password_correct(entered_password=password):
            return 'Доступ разрешен'
        else:
            return 'Доступ запрещен'

    def __is_password_correct(self, entered_password):
        return User.__encode_password(entered_password) == self.__password

    @staticmethod
    def __encode_password(password):
        encoded_password = password.encode()
        return bcrypt.hashpw(encoded_password, password_salt)
