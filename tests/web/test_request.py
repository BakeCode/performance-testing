import unittest
from performance.web import Request, RequestTypeError, RequestTimeError


class RequestTestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'http://www.google.com'

    def test_constants(self):
        self.assertEqual('get', Request.GET)
        self.assertEqual('post', Request.POST)

    def test_init(self):
        request = Request(url=self.url, type=Request.GET)
        self.assertEqual(self.url, request.url)
        self.assertEqual(Request.GET, request.type)

    def test_do(self):
        request = Request(url=self.url, type=Request.GET)
        request.do()
        self.assertTrue(hasattr(request, 'status_code'))
        request.type = Request.POST
        request.do()
        self.assertTrue(hasattr(request, 'status_code'))

    def test_invalid_type(self):
        type = 'foo_bar'
        request = Request(url=self.url, type=type)
        with self.assertRaises(RequestTypeError) as error:
            request.do()
        self.assertEqual('Invalid request type "%s"' % type, error.exception.__str__())

    def test_response_time(self):
        request = Request(url=self.url, type=Request.GET)
        request.do()
        self.assertEqual(request.finished - request.started, request.get_response_time())

    def test_time_error(self):
        request = Request(url=self.url, type=Request.GET)
        with self.assertRaises(RequestTimeError):
            request.get_response_time()
