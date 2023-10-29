import json
from http import HTTPStatus
import error_handlers
from utils import parse_query_string
from github_worker import GithubWorker


def main(environ, start_response):
    if environ['REQUEST_METHOD'] != 'GET':
        return error_handlers.method_not_allowed(start_response)

    query_dict = parse_query_string(environ['QUERY_STRING'])
    if query_code := query_dict.get('query_code'):
        if not query_code.isdigit():
            return error_handlers.bad_request(start_response, 'параметр query_code должен быть числом')
        query_code = int(query_code)
        if query_code not in (status.value for status in HTTPStatus):
            return error_handlers.bad_request(start_response, 'указан некорректный query_code')
        http_status = HTTPStatus(query_code)
        resp = json.dumps({
            'status': http_status.value,
            'detail': http_status.name,
        })
        bytes_resp = bytes(resp, 'utf-8')
        start_response(f'{http_status.value} {http_status.name}', [('Content-Type', 'application/json')])
        return [bytes_resp]

    resp = json.dumps({
        'detail': 'Чтобы получить определенный Http-статус, укажите его номер в параметре query_code',
    })
    bytes_resp = bytes(resp, 'utf-8')
    start_response('200 OK', [('Content-Type', 'application/json')])
    return [bytes_resp]


def repos(environ, start_response):
    if environ['REQUEST_METHOD'] != 'GET':
        return error_handlers.method_not_allowed(start_response)

    token = environ.get('HTTP_AUTHORIZATION')
    github = GithubWorker(github_token=token)
    if not token or not github.is_token_correct():
        return error_handlers.unauthorized(start_response)

    user_repos = github.get_repos()
    serialized_repos = [
        {
            'name': repo['name'],
            'repo_url': repo['html_url'],
            'visibility': repo['visibility'],
            'subscribers_count': len(github.get_repo_subscribers(user=repo['owner']['login'], repo_name=repo['name'])),
            'size': repo['size'],
        } for repo in user_repos
    ]
    resp = json.dumps(serialized_repos)
    bytes_resp = bytes(resp, 'utf-8')
    start_response('200 OK', [('Content-Type', 'application/json')])
    return [bytes_resp]
