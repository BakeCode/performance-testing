import unittest
from performance.web import Response


class ResponseTestCase(unittest.TestCase):
    def test_init(self):
        url = '/foo/bar'
        time = 23.203
        code = 200
        response = Response(url=url, time=time, code=code)
        self.assertEqual(url, response.url)
        self.assertEqual(time, response.time)
        self.assertEqual(code, response.code)

    def test_to_string(self):
        url = '/foo/bar'
        time = 23.203
        code = 200
        response = Response(url=url, time=time, code=code)
        self.assertEqual(
            '   %s   %.4f   %d' % (url, time, code),
            response.__str__()
        )
