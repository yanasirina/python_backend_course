from datetime import datetime
from functools import reduce


def flatten(array):
    result = []
    for i in array:
        if type(i) in (list, tuple, set):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result


def convert_obj_to_int(obj):
    if isinstance(obj, int):
        return obj
    if isinstance(obj, str) and obj.strip().isdigit():
        return int(obj)
    else:
        raise ValueError(f'аргумент {obj} типа {type(obj)} поступил в функцию {convert_obj_to_int.__name__}, '
                         f'но не может быть обработан.')


def get_flat_int_args(fn):
    def wrapper(*args):
        start_time = datetime.now()
        print(f"Запуск функции: {fn.__name__}(), с аргументами: {args}")

        flatten_args = flatten(args)
        correct_args = []

        for arg in flatten_args:
            arg = convert_obj_to_int(arg)
            correct_args.append(arg)

        print(f"Аргументы после преобразования: {correct_args}")
        result = fn(*correct_args)

        print(f'Функция выполнена за {datetime.now() - start_time}')
        return result
    return wrapper


@get_flat_int_args
def get_nested_args_sum(*args):
    summa = reduce(lambda x, y: x + y, args)
    return summa


if __name__ == '__main__':
    nested_args = list([[1, 2], [3, 4, [7, "9", "11"], {1, ("0", 17)}]])
    args_sum = get_nested_args_sum(nested_args)
    print(f'Сумма аргументов функции: {args_sum}')
