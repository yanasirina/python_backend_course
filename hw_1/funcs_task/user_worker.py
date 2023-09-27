from dataclasses import dataclass
from typing import Union


class UserException(Exception):
    """Обработка исключений, связанных с пользователями"""


@dataclass
class User:
    name: str
    age: int


def user_to_dataclass(user: Union[list, tuple, str, dict]) -> User:
    if isinstance(user, (list, tuple)):
        name, age = user
    elif isinstance(user, str):
        name, age = user.split()
    elif isinstance(user, dict):
        name, age = user["name"], user["age"]
    else:
        raise UserException('Unhandled user type')

    return User(name=name, age=age)
