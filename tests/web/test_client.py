import unittest
from performance.web import Client, Request
from performance.result import Result
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
            client_name='client_0',
            result=Result()
        )
        self.assertListEqual(requests, client.requests)
        self.assertEqual(requests_counter, client.counter)
        self.assertTrue(isinstance(client.result, Result))

    def test_run(self):
        requests = [
            Request(url='/'),
            Request(url='/about'),
            Request(url='/imprint')
        ]
        requests_counter = 5
        run_event = Event()
        run_event.set()
        client_name = 'client_0'
        client = Client(
            host=self.host,
            requests=requests,
            do_requests_counter=requests_counter,
            run_event=run_event,
            client_name=client_name,
            result=Result()
        )
        client.run()
        self.assertEqual(0, client.counter)
        self.assertEqual(requests_counter * len(requests), len(client.responses))
        stream = open('result/%s.json' % client_name, 'r')
        content = json.loads(stream.read())
        stream.close
        keys = [
            '%s%s' % (client_name, requests[0].url),
            '%s%s' % (client_name, requests[1].url),
            '%s%s' % (client_name, requests[2].url)
        ]
        for key in keys:
            self.assertTrue(key in content)
            self.assertEqual(requests_counter, len(content[key]))

        client = Client(
            host=self.host,
            requests=requests,
            do_requests_counter=-1,
            run_event=run_event,
            client_name=client_name,
            result=Result()
        )
        client.run()

    def test_write_to_file(self):
        client_name = 'client_0'
        client = Client(
            host=None,
            requests=None,
            do_requests_counter=None,
            run_event=None,
            client_name=client_name,
            result=Result()
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
