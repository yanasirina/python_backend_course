class FibonacciIterator:
    def __init__(self):
        self.previous = 0
        self.current = 1

    def __next__(self):
        current_number = self.current
        self.previous, self.current = self.current, self.current + self.previous
        return current_number

    def __iter__(self):
        return self


if __name__ == '__main__':
    fibonacci_iterator = FibonacciIterator()
    for _ in range(10):
        print(next(fibonacci_iterator))
