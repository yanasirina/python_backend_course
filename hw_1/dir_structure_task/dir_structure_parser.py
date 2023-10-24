import sys
import argparse
import os


def create_parser() -> argparse.ArgumentParser:
    description = 'Для получения древовидной структуры папки - укажите полный путь к ней в параметре name'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-n', '--name', required=True)
    return parser


def get_relative_path(absolute_path: str) -> str:
    return absolute_path.strip('/').split('/')[-1]


def get_dir_structure(absolute_path: str, level: int = 0):
    relative_path = get_relative_path(absolute_path)
    print('---' * level, relative_path)

    dirs = os.listdir(absolute_path)
    for inside_element in dirs:
        inside_absolute_path = absolute_path + inside_element + '/'
        if os.path.isdir(inside_absolute_path):
            get_dir_structure(absolute_path=inside_absolute_path, level=level+1)
        else:
            inside_relative_path = get_relative_path(inside_absolute_path)
            file_size = os.path.getsize(inside_absolute_path[:-1])
            print('---' * (level + 1), inside_relative_path, f'({file_size} б)')


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    get_dir_structure(namespace.name)
