from performance import web


class Tool:
    def __init__(self, config):
        if not isinstance(config, Config):
            raise TypeError('No performance.routine.Config object')
        self.config = config

    def run(self):
        clients = []
        for client_index in range(self.config.clients_count):
            client = web.Client(
                host=self.config.host,
                requests=self.config.requests,
                do_requests_counter=self.config.requests_per_client
            )
            clients.append(client)
            client.start()


class Config:
    def __init__(self, host, requests_per_client=10, clients_count=1):
        self.host = host
        self.requests = []
        self.requests_per_client = requests_per_client
        self.clients_count = clients_count

    def add_request(self, request):
        if not isinstance(request, web.Request):
            raise TypeError('No performance.web.Request object')
        self.requests.append(request)
