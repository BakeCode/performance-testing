import requests
from time import time


class Client:
    def __init__(self):
        pass


class Request:
    GET = 'get'
    POST = 'post'

    def __init__(self, url, type, data=None):
        self.url = url
        self.type = type
        self.data = data

    def do(self):
        try:
            data = ''
            if isinstance(self.data, RequestData):
                data = self.data.for_type(type=self.type)
            self.started = time()
            response = getattr(requests, self.type)(
                url=self.url,
                data=data
            )
            self.finished = time()
            self.status_code = response.status_code
        except AttributeError:
            raise RequestTypeError(type=self.type)

    def get_response_time(self):
        try:
            return self.finished - self.started
        except AttributeError:
            raise RequestTimeError


class RequestData:
    def __init__(self, data=None):
        self.data = data

    def for_type(self, type=Request.GET):
        if type is Request.GET:
            return data


class RequestTypeError(Exception):
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return 'Invalid request type "%s"' % self.type


class RequestTimeError(Exception):
    pass
