import unittest
from performance.web import Request, RequestTypeError, Response, RequestData


class RequestTestCase(unittest.TestCase):
    def setUp(self):
        self.host = 'http://www.google.com'

    def test_constants(self):
        self.assertEqual('get', Request.GET)
        self.assertEqual('post', Request.POST)

    def test_init(self):
        request = Request(url=self.host)
        self.assertEqual(Request.GET, request.type)
        self.assertEqual(self.host, request.url)
        request = Request(url=self.host, type=Request.POST)
        self.assertEqual(Request.POST, request.type)

    def test_do(self):
        request = Request(url='/', type=Request.GET)
        response = request.do(host=self.host)
        self.assertTrue(isinstance(response, Response))

        request = Request(url='/', type=Request.GET, data=RequestData(data=''))
        response = request.do(host=self.host)
        self.assertTrue(isinstance(response, Response))

    def test_invalid_type(self):
        type = 'foo_bar'
        request = Request(url=self.host, type=type)
        with self.assertRaises(RequestTypeError) as error:
            request.do(host=self.host)
        self.assertEqual('Invalid request type "%s"' % type, error.exception.__str__())
