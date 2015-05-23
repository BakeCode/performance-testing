from performance import web
import time
import threading


class Tool:
    def __init__(self, config):
        if not isinstance(config, Config):
            raise TypeError('No performance.routine.Config object')
        self.config = config

    def run(self):
        if self.config.is_valid():
            run_event = threading.Event()
            run_event.set()
            clients = []
            print(' > Started tests')
            print(' > Stop tests with CTRL-C')
            try:
                start_time = time.time()
                for client_index in range(self.config.clients_count):
                    client = web.Client(
                        host=self.config.host,
                        requests=self.config.requests,
                        do_requests_counter=self.config.requests_per_client,
                        run_event=run_event,
                        client_name='client_%d' % client_index
                    )
                    clients.append(client)
                    client.start()
                for client in clients:
                    client.join()
                end_time = time.time()
                total_requests = self.config.requests_per_client * self.config.clients_count * len(self.config.requests)
                print(' > Finished %d tests in %.2f seconds' % (total_requests, end_time - start_time))
            except KeyboardInterrupt:
                run_event.clear()
                print(' > Exited with CTRL-C')
        else:
            print(' > Invalid configuration')


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

    def is_valid(self):
        return not(
            not self.requests
            or
            self.clients_count < 1
            or
            self.requests_per_client < 1
        )
