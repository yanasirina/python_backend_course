from abc import ABC, abstractmethod, abstractproperty
import asyncio
import aiohttp
import httpx


class AbstractAsyncWebWorker(ABC):
    """Абстрактный класс для асинхронного получения информации с веб-страниц"""

    def __init__(self, url):
        self.url = url

    @abstractmethod
    async def get_response(self):
        """Получение ответа по запрашиваемой странице"""

    @abstractproperty
    async def status_code(self):
        """Получение статуса запрашиваемой страницы"""


class HttpxWebWorker(AbstractAsyncWebWorker):
    """Класс для получения информации с веб-страниц с помощью библиотеки httpx"""
    def __init__(self, *args, httpx_client, **kwargs):
        super().__init__(*args, **kwargs)
        self._client = httpx_client

    async def get_response(self):
        response = await self._client.get(self.url)
        return response

    @property
    async def status_code(self):
        response = await self.get_response()
        return response.status_code


class AiohttpWebWorker(AbstractAsyncWebWorker):
    """Класс для получения информации с веб-страниц с помощью библиотеки aiohttp"""
    def __init__(self, *args, aiohttp_session, **kwargs):
        super().__init__(*args, **kwargs)
        self._session = aiohttp_session

    async def get_response(self):
        response = await self._session.get(url=self.url)
        return response

    @property
    async def status_code(self):
        response = await self.get_response()
        return response.status


async def httpx_func():
    async with httpx.AsyncClient() as client:
        httpx_example_worker = HttpxWebWorker(url='https://example.com', httpx_client=client)
        tasks = [asyncio.create_task(httpx_example_worker.status_code) for _ in range(5)]
        statuses = await asyncio.gather(*tasks)
        print(statuses)


async def aiohttp_func():
    async with aiohttp.ClientSession() as session:
        aiohttp_example_worker = AiohttpWebWorker(url='https://example.com', aiohttp_session=session)
        tasks = [asyncio.create_task(aiohttp_example_worker.status_code) for _ in range(5)]
        statuses = await asyncio.gather(*tasks)
        print(statuses)


if __name__ == '__main__':
    asyncio.run(httpx_func())
    asyncio.run(aiohttp_func())
