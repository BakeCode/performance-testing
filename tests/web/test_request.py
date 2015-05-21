import unittest
from performance.web import Request, RequestTypeError


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
        request = Request(url=self.host, type=Request.GET)
        request.do()

    def test_invalid_type(self):
        type = 'foo_bar'
        request = Request(url=self.host, type=type)
        with self.assertRaises(RequestTypeError) as error:
            request.do()
        self.assertEqual('Invalid request type "%s"' % type, error.exception.__str__())
