import unittest
from performance_testing.config import Config, Request
from performance_testing.errors import ConfigError


class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.config.host = 'http://www.example.com'
        self.config.requests = [
            Request(url='/', type='GET', data=''),
            Request(url='/about', type='GET', data=''),
            Request(url='/imprint', type='GET', data='')
        ]

    def test_check_valid(self):
        config = Config()
        with self.assertRaises(ConfigError) as error:
            config.check_valid()
        self.assertEqual(error.exception.message, 'Config with name "host" not set.')
        config.host = 'http://www.example.com'

        with self.assertRaises(ConfigError) as error:
            config.check_valid()
        self.assertEqual(error.exception.message, 'Config with name "requests_count" not set.')
        config.requests_count = 10

        with self.assertRaises(ConfigError) as error:
            config.check_valid()
        self.assertEqual(error.exception.message, 'Config with name "clients_count" not set.')
        config.clients_count = 2

        with self.assertRaises(ConfigError) as error:
            config.check_valid()
        self.assertEqual(error.exception.message, 'Config with name "requests" not set.')
        config.requests = [
            Request(url='/', type='GET', data=''),
            Request(url='/about', type='GET', data=''),
            Request(url='/imprint', type='GET', data='')
        ]

    def test_url(self):
        self.assertEqual('http://www.example.com/',
                         self.config.url(self.config.requests[0].url))
        self.assertEqual('http://www.example.com/about',
                         self.config.url(self.config.requests[1].url))
        self.assertEqual('http://www.example.com/imprint',
                         self.config.url(self.config.requests[2].url))

    def test_request_init(self):
        url = '/the/url'
        type = 'GET'
        data = 'foo=bar&bla=blubb'
        request = Request(url=url, type=type, data=data)
        self.assertEqual(request.url, url)
        self.assertEqual(request.type, type)
        self.assertEqual(request.data, data)
