import unittest
from performance.web import RequestData, Request


class RequestDataTestCase(unittest.TestCase):
    def setUp(self):
        self.host = 'http://www.google.com'

    def test_init(self):
        request_data = RequestData()
        self.assertIsNone(request_data.data)
        request_data = RequestData(data={})
        self.assertDictEqual({}, request_data.data)

    def test_get_converted(self):
        data = {'foo': 'bar'}
        request_data = RequestData(data=data)
        self.assertDictEqual(data, request_data.get_converted(type=Request.GET))
        self.assertNotEqual(data, request_data.get_converted(type=Request.POST))
