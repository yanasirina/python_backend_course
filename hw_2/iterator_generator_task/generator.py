def get_fibonacci():
    previous_number = 0
    current_number = 1
    while True:
        yield current_number
        previous_number, current_number = current_number, current_number + previous_number


if __name__ == '__main__':
    fibonacci_generator = get_fibonacci()
    for _ in range(10):
        print(next(fibonacci_generator))
