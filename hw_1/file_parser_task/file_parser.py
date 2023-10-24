def print_binary_file_data(path: str):
    with open(path, 'rb') as file:
        decoded_file_data = file.read().decode()
        print('Содержимое файла:', decoded_file_data, sep='\n')
        print('Количество символов в файле:', len(decoded_file_data))
        print('Количество слов в файле:', len(decoded_file_data.split()))
        print('Количество строк в файле:', decoded_file_data.count('\n') + 1)


if __name__ == '__main__':
    print_binary_file_data('file.bin')
