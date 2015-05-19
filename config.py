from performance_testing.config import Config, Request


CONFIG = Config()
CONFIG.host = 'http://www.example.com'
CONFIG.clients_count = 2
CONFIG.requests_count = 10
CONFIG.requests = [
    Request(url='/', type='GET', data=''),
    Request(url='/about', type='GET', data='')
]
