import unittest
from performance.web import Client


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.host = 'http://www.google.com'

    def test_init(self):
        requests = []
        requests_counter = 10
        client = Client(host=self.host, requests=requests, do_requests_counter=requests_counter)
        self.assertListEqual(requests, client.requests)
        self.assertEqual(requests_counter, client.counter)
