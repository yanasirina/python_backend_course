import requests
from urllib.parse import urljoin


class GithubWorker:
    BASE_URL = 'https://api.github.com/user'

    def __init__(self, github_token: str):
        self.github_token = github_token

    def get_repos(self):
        response = self._request(path='user/repos')
        return response

    def get_repo_subscribers(self, user: str, repo_name: str):
        response = self._request(path=f'repos/{user}/{repo_name}/subscribers')
        return response

    def is_token_correct(self):
        response = requests.get(url=self.BASE_URL, headers={'Authorization': f'Bearer {self.github_token}'})
        if response.ok:
            return True
        elif response.status_code == 401:
            return False
        else:
            response.raise_for_status()

    def _get_headers(self) -> dict:
        headers = {
            'Authorization': f'Bearer {self.github_token}'
        }
        return headers

    def _request(self, path: str, method: str = 'get', params: dict = None, data: dict = None):
        assert not method or method in ('get', 'post', 'put', 'patch', 'delete')

        url = urljoin(self.BASE_URL, path)
        response = requests.request(method=method, url=url, params=params, data=data, headers=self._get_headers())
        response.raise_for_status()
        return response.json()
