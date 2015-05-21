from performance import web


class Tool:
    def __init__(self, config):
        if not isinstance(config, Config):
            raise TypeError('No performance.routine.Config object')
        self.config = config

    def run(self):
        pass


class Config:
    def __init__(self, host, requests=None, requests_per_client=10, clients_count=1):
        self.host = host
        if requests is None:
            self.requests = []
        else:
            self.requests = requests
        self.requests_per_client = requests_per_client
        self.clients_count = clients_count

    def add_request(self, request):
        if not isinstance(request, web.Request):
            raise TypeError('No performance.web.Request object')
        self.requests.append(request)
