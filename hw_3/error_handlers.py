import json
from typing import List


def bad_request(start_response, err_text: str = None) -> List[bytes]:
    resp = json.dumps({
        'error': err_text or 'Ошибка запроса',
        'status': 400
    })
    bytes_resp = bytes(resp, 'utf-8')
    start_response('400 Bad Request', [('Content-Type', 'application/json')])
    return [bytes_resp]


def method_not_allowed(start_response, err_text: str = None) -> List[bytes]:
    resp = json.dumps({
        'error': err_text or 'Для приложения доступен только метод GET',
        'status': 405
    })
    bytes_resp = bytes(resp, 'utf-8')
    start_response('405 Method Not Allowed', [('Content-Type', 'application/json')])
    return [bytes_resp]


def page_not_found(start_response, err_text: str = None) -> List[bytes]:
    resp = json.dumps({
        'error': err_text or 'Страница не найдена',
        'status': 404

    })
    bytes_resp = bytes(resp, 'utf-8')
    start_response('404 Not Found', [('Content-Type', 'application/json')])
    return [bytes_resp]


def unauthorized(start_response, err_text: str = None) -> List[bytes]:
    resp = json.dumps({
        'error': err_text or 'Пользователь не авторизован',
        'status': 401
    })
    bytes_resp = bytes(resp, 'utf-8')
    start_response('401 Unauthorized', [('Content-Type', 'application/json')])
    return [bytes_resp]
