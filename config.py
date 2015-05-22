from performance.routine import Config
from performance.web import Request

CONFIG = Config(host='http://www.example.com', requests_per_client=10, clients_count=3)
CONFIG.add_request(Request(url='/'))
