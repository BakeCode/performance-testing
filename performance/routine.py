from performance import web


class Tool:
    def __init__(self, config):
        if not isinstance(config, Config):
            raise TypeError('No performance.routine.Config object')
        self.config = config

    def run(self):
        pass


class Config:
    def __init__(self, host, requests=[], do_requests_count=10, clients_count=1):
        self.host = host
        self.requests = requests
        self.do_requests_count = do_requests_count
        self.clients_count = clients_count

    def add_request(self, request):
        if not isinstance(request, web.Request):
            raise TypeError('No performance.web.Request object')
        self.requests.append(request)
