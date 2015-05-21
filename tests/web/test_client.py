import unittest
from performance.web import Client, Request
from performance.routine import FinishEvent
from threading import Event
import json


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.host = 'http://www.google.com'

    def test_init(self):
        requests = []
        requests_counter = 10
        client = Client(
            host=self.host,
            requests=requests,
            do_requests_counter=requests_counter,
            run_event=Event(),
            finish_event=FinishEvent(),
            client_name='client_1.json'
        )
        self.assertListEqual(requests, client.requests)
        self.assertEqual(requests_counter, client.counter)
    def test_write_to_file(self):
        client_name = 'client_0'
        client = Client(
            host=None,
            requests=None,
            do_requests_counter=None,
            run_event=None,
            finish_event=None,
            client_name=client_name
        )
        data = {
            'foo': 'bar',
            'blubb': 32,
            'bla': False
        }
        client.write_to_file(data=data)
        stream = open('result/%s.json' % client_name, 'r')
        content = json.loads(stream.read())
        stream.close
        self.assertEqual(data, content)
