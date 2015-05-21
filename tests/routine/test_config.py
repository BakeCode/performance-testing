import unittest
from performance.routine import Config
from performance.web import Request


class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.host = 'http://www.google.com'

    def test_init(self):
        config = Config(host=self.host)
        self.assertEqual(self.host, config.host)
        self.assertListEqual([], config.requests)
        self.assertEqual(10, config.requests_per_client)
        self.assertEqual(1, config.clients_count)

    def test_add_request(self):
        config = Config(host='config_host')
        request_a = Request(url='/', type=Request.GET)
        request_b = Request(url='/about', type=Request.POST)
        config.add_request(request_a)
        config.add_request(request_b)
        self.assertListEqual([request_a, request_b], config.requests)
        with self.assertRaises(TypeError) as error:
            config.add_request('no_request_type')
        self.assertEqual('No performance.web.Request object', error.exception.__str__())

    def test_is_valid(self):
        config = Config(host='config_host')
        self.assertFalse(config.is_valid())

        config = Config(host='config_host')
        config.requests_per_client = 0
        config.add_request(Request(url='/', type=Request.GET))
        self.assertFalse(config.is_valid())

        config = Config(host='config_host')
        config.clients_count = 0
        config.add_request(Request(url='/', type=Request.GET))
        self.assertFalse(config.is_valid())

        config = Config(host='config_host')
        config.add_request(Request(url='/', type=Request.GET))
        self.assertTrue(config.is_valid())
