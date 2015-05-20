import unittest
from performance.routine import Config
from performance.web import Request


class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.host = 'http://www.google.com'

    def test_init(self):
        config = Config(host=self.host)
        self.assertEqual(self.host, config.host)
        self.assertEqual([], config.requests)

    def test_add_request(self):
        config = Config(host=self.host)
        requestA = Request(url='/', type=Request.GET)
        requestB = Request(url='/about', type=Request.POST)
        config.add_request(requestA)
        config.add_request(requestB)
        self.assertEqual([requestA, requestB], config.requests)
        with self.assertRaises(TypeError) as error:
            config.add_request('no_request_type')
        self.assertEqual('No performance.web.Request object', error.exception.__str__())
