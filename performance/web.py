import requests
from time import time
from threading import Thread
import json


class Client(Thread):
    def __init__(self, host, requests, do_requests_counter, run_event, finish_event, client_name):
        super(Client, self).__init__()
        self.host = host
        self.requests = requests
        self.counter = do_requests_counter
        self.run_event = run_event
        self.finish_event = finish_event
        self.client_name = client_name
        self.responses = []

    def run(self):
        url_times = {}
        while 0 < self.counter and self.run_event.is_set():
            for request in self.requests:
                key = self.client_name + request.url
                if not key in url_times:
                    url_times[key] = []
                response = request.do(host=self.host)
                url_times[key].append(round(response.time(), 5))
                self.responses.append(response)
            self.counter = self.counter - 1
        if self.counter is 0:
            print(' > Finished a client')
            stream = open('result/%s.json' % self.client_name, 'w')
            stream.write(json.dumps(url_times))
            stream.close()
        else:
            print(' > Interrupted a client')
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
            try:
                response = getattr(requests, self.type)(
                    url=host + self.url,
                    data=data,
                    timeout=10
                )
                finished = time()
                return Response(
                    url=self.url,
                    started=started,
                    finished=finished,
                    code=response.status_code
                )
            except requests.exceptions.Timeoute:
                return Response(
                    url=self.url,
                    started=0,
                    finished=0,
                    code=0
                )
        except AttributeError:
            raise RequestTypeError(type=self.type)


class Response:
    def __init__(self, url, started, finished, code):
        self.url = url
        self.started = started
        self.finished = finished
        self.code = code

    def time(self):
        return self.finished - self.started

    def __str__(self):
        return '   %s   %.4f   %d' % (self.url, self.time(), self.code)

    def to_dictionary(self):
        return {
            'code': self.code,
            'started': self.started,
            'time': self.time()
        }


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
