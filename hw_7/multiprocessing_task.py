import multiprocessing
import os
import time
from typing import Callable


def get_fib(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return get_fib(n - 1) + get_fib(n - 2)


def get_time_per_func_with_multiprocessing(func: Callable, processes_count: int) -> float:
    start_time = time.perf_counter()
    processes = []

    for _ in range(processes_count):
        process = multiprocessing.Process(target=func, args=(35,))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()

    end_time = time.perf_counter()
    total_time = end_time - start_time
    time_per_func = total_time / processes_count
    return time_per_func


if __name__ == '__main__':
    processes_count = os.cpu_count()
    for i in range(1, processes_count + 1):
        time_per_func = get_time_per_func_with_multiprocessing(func=get_fib, processes_count=i)
        print(f'На каждый вызов функции было затрачено {time_per_func:.4f} секунд при запуске {i} процессов')
