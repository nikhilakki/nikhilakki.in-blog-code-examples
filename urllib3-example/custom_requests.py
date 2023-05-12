# Copyright (c) 2023 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Optional, Dict, Any
import urllib3

class CustomRequests:
    def __init__(self) -> None:
        self.session: urllib3.PoolManager = urllib3.PoolManager()

    def get(self, url: str, **kwargs: Any) -> 'CustomResponse':
        response: urllib3.HTTPResponse = self.session.request('GET', url, **kwargs)
        return CustomResponse(response)

    def post(self, url: str, data: Optional[bytes] = None, json: Optional[Dict[str, Any]] = None, **kwargs: Any) -> 'CustomResponse':
        if json:
            kwargs['body'] = json
            headers = kwargs.pop('headers', {})
            headers['Content-Type'] = 'application/json'
            kwargs['headers'] = headers
        elif data:
            kwargs['body'] = data
        response: urllib3.HTTPResponse = self.session.request('POST', url, **kwargs)
        return CustomResponse(response)

    def put(self, url: str, data: Optional[bytes] = None, **kwargs: Any) -> 'CustomResponse':
        if data:
            kwargs['body'] = data
        response: urllib3.HTTPResponse = self.session.request('PUT', url, **kwargs)
        return CustomResponse(response)

    def delete(self, url: str, **kwargs: Any) -> 'CustomResponse':
        response: urllib3.HTTPResponse = self.session.request('DELETE', url, **kwargs)
        return CustomResponse(response)


class CustomResponse:
    def __init__(self, response: urllib3.HTTPResponse) -> None:
        self.response: urllib3.HTTPResponse = response

    @property
    def content(self) -> bytes:
        return self.response.data

    @property
    def text(self) -> str:
        return self.response.data.decode('utf-8')

    @property
    def status_code(self) -> int:
        return self.response.status

if __name__ == "__main__":
    custom_requests = CustomRequests()
    response = custom_requests.get('https://jsonplaceholder.typicode.com/todos/1')
    print(response.text)