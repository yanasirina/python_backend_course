with open('file.bin', 'rb') as file:
    decoded_file_data = file.read().decode()
    print('Содержимое файла:', decoded_file_data, sep='\n')
    print('Количество символов в файле:', len(decoded_file_data))
    print('Количество слов в файле:', len(decoded_file_data.split()))
    print('Количество строк в файле:', decoded_file_data.count('\n') + 1)
