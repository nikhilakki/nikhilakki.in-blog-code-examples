# Copyright (c) 2023 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import urllib3

class CustomRequests:
    def __init__(self):
        self.session = urllib3.PoolManager()

    def get(self, url, **kwargs):
        response = self.session.request('GET', url, **kwargs)
        return CustomResponse(response)

    def post(self, url, data=None, json=None, **kwargs):
        if json:
            kwargs['body'] = json
            headers = kwargs.pop('headers', {})
            headers['Content-Type'] = 'application/json'
            kwargs['headers'] = headers
        elif data:
            kwargs['body'] = data
        response = self.session.request('POST', url, **kwargs)
        return CustomResponse(response)

    def put(self, url, data=None, **kwargs):
        if data:
            kwargs['body'] = data
        response = self.session.request('PUT', url, **kwargs)
        return CustomResponse(response)

    def delete(self, url, **kwargs):
        response = self.session.request('DELETE', url, **kwargs)
        return CustomResponse(response)


class CustomResponse:
    def __init__(self, response):
        self.response = response

    @property
    def content(self):
        return self.response.data

    @property
    def text(self):
        return self.response.data.decode('utf-8')

    @property
    def status_code(self):
        return self.response.status


if __name__ == "__main__":
    custom_requests = CustomRequests()
    response = custom_requests.get('https://jsonplaceholder.typicode.com/todos/1')
    print(response.text)