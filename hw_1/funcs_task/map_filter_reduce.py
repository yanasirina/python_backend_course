from functools import reduce

from consts import MIN_ALLOWED_AGE
from user_worker import user_to_dataclass

if __name__ == '__main__':
    # reduce
    words_list = ['Privet', 'Mir']
    words_str = reduce(lambda x, y: x.lower() + ' ' + y.lower(), words_list)
    print(words_str)

    # filter (выбирает только пользователей разрешенного возраста)
    users = [{'name': 'Alex', 'age': 18}, {'name': 'Maria', 'age': 14}, {'name': 'Valeria', 'age': 28},
             {'name': 'Ivan', 'age': 16}, {'name': 'Gleb', 'age': 30}, {'name': 'Petr', 'age': 13}]
    allowed_users = list(filter(lambda user: user['age'] >= MIN_ALLOWED_AGE, users))
    print(allowed_users)

    # map (преобразует пользователей разных типов к одному
    users = [{'name': 'Alex', 'age': 18}, ('Maria', 14), 'Valeria 28', ['Ivan', 16]]
    user_dataclasses = list(map(user_to_dataclass, users))
    print(user_dataclasses)
