import unittest
from performance_testing.config import Config, Request
from performance_testing.errors import ConfigError


class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.config = Config()

    def test_check_valid(self):
        with self.assertRaises(ConfigError) as error:
            self.config.check_valid()
        self.assertEqual(error.exception.message, 'Config with name "host" not set.')
        self.config.host = 'http://www.example.com'

        with self.assertRaises(ConfigError) as error:
            self.config.check_valid()
        self.assertEqual(error.exception.message, 'Config with name "requests_count" not set.')
        self.config.requests_count = 10

        with self.assertRaises(ConfigError) as error:
            self.config.check_valid()
        self.assertEqual(error.exception.message, 'Config with name "clients_count" not set.')
        self.config.clients_count = 2

        with self.assertRaises(ConfigError) as error:
            self.config.check_valid()
        self.assertEqual(error.exception.message, 'Config with name "requests" not set.')
        self.config.requests = [
            Request(url='/', type='GET', data=''),
            Request(url='/about', type='GET', data=''),
            Request(url='/imprint', type='GET', data='')
        ]
