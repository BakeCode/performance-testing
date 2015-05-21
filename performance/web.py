import requests
from time import time
from threading import Thread


class Client(Thread):
    def __init__(self, host, requests, do_requests_counter, event, finish_event):
        super(Client, self).__init__()
        self.host = host
        self.requests = requests
        self.counter = do_requests_counter
        self.event = event
        self.finish_event = finish_event

    def run(self):
        while 0 < self.counter and self.event.is_set():
            for request in self.requests:
                print('%s - %.4f' % (request.url, request.do(host=self.host)))
            self.counter = self.counter - 1
        self.finish_event.finish()


class Request:
    GET = 'get'
    POST = 'post'

    def __init__(self, url, type=GET, data=None):
        self.url = url
        self.type = type
        self.data = data

    def do(self, host):
        try:
            data = ''
            if isinstance(self.data, RequestData):
                data = self.data.for_type(type=self.type)
            started = time()
            response = getattr(requests, self.type)(
                url=host + self.url,
                data=data
            )
            finished = time()
            return finished - started
        except AttributeError:
            raise RequestTypeError(type=self.type)


class RequestData:
    def __init__(self, data=None):
        self.data = data

    def get_converted(self, type=Request.GET):
        if type is Request.GET:
            return self.data


class RequestTypeError(Exception):
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return 'Invalid request type "%s"' % self.type
