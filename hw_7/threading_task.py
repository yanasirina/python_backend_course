import threading

import requests


def get_data_from_url(url: str):
    print(f'start {url}')
    response = requests.get(url)
    print(f'{url} info:\n'
          f'status {response.status_code},\n'
          f'content length {len(response.content)},\n'
          f'text length {len(response.text)}')


if __name__ == '__main__':
    urls = ['https://www.google.com/', 'https://example.com/', 'https://www.python.org/']
    threads = []

    for url in urls:
        thread = threading.Thread(target=get_data_from_url, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
