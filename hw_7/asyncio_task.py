"""
Этого задания не было в курсе, но я заметила ошибку в лекции, поэтому решила ее здесь исправить.
Ошибка заключалась в том, что при демонстрации асинхронного подхода написания кода,
пример на самом деле работал синхронно.
"""


import asyncio
from aiohttp import ClientSession
import time


async def call_url(url):
    """Функция из лекции"""
    print(f'Starting {url}')
    async with ClientSession() as session:
        response = await session.get(url)
        data = await response.text()
        print(f'{url}: {response.status}')
        return data


async def main():
    urls = ['https://www.google.com/', 'https://example.com/', 'https://www.python.org/']

    # вариант из лекции (работает синхронно)
    start_time = time.perf_counter()
    tasks = [call_url(url) for url in urls]
    for task in tasks:
        await task
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'Вариант из лекции завершился за {total_time:.4f} сек.')
    """
    Starting https://www.google.com/
    https://www.google.com/: 200
    Starting https://example.com/
    https://example.com/: 200
    Starting https://www.python.org/
    https://www.python.org/: 200
    Вариант из лекции завершился за 1.5334 сек.
    """

    # асинхронный вариант 1
    start_time = time.perf_counter()
    tasks = [asyncio.create_task(call_url(url)) for url in urls]
    for task in tasks:
        await task
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'Асинхронный вариант 1 завершился за {total_time:.4f} сек.')
    """
    Вариант из лекции завершился за 1.5334 сек.
    Starting https://www.google.com/
    Starting https://example.com/
    Starting https://www.python.org/
    https://www.google.com/: 200
    https://www.python.org/: 200
    https://example.com/: 200
    Асинхронный вариант 1 завершился за 0.7767 сек.
    """

    # асинхронный вариант 2
    start_time = time.perf_counter()
    tasks = [call_url(url) for url in urls]
    await asyncio.gather(*tasks)  # gather, as_completed, wait (с wait все равно лучше использовать задачи)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'Асинхронный вариант 2 завершился за {total_time:.4f} сек.')
    """
    Starting https://www.google.com/
    Starting https://example.com/
    Starting https://www.python.org/
    https://www.google.com/: 200
    https://www.python.org/: 200
    https://example.com/: 200
    Асинхронный вариант 2 завершился за 0.7617 сек.
    """


if __name__ == '__main__':
    asyncio.run(main())
