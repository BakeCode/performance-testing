import unittest
from performance.web import Response


class ResponseTestCase(unittest.TestCase):
    def setUp(self):
        self.url = '/foo/bar'
        self.started = 23.2032139
        self.finished = 42.2321123
        self.time = self.finished - self.started
        self.code = 200

    def test_init(self):
        response = Response(
            url=self.url,
            started=self.started,
            finished=self.finished,
            code=self.code
        )
        self.assertEqual(self.url, response.url)
        self.assertEqual(self.started, response.started)
        self.assertEqual(self.finished, response.finished)
        self.assertEqual(self.code, response.code)

    def test_time(self):
        response = Response(
            url=self.url,
            started=self.started,
            finished=self.finished,
            code=self.code
        )
        self.assertEqual(self.time, response.time())

    def test_to_string(self):
        response = Response(
            url=self.url,
            started=self.started,
            finished=self.finished,
            code=self.code
        )
        self.assertEqual(
            '   %s   %.4f   %d' % (self.url, self.time, self.code),
            response.__str__()
        )

    def test_to_dictionary(self):
        dictionary = {
            'code': self.code,
            'started': self.started,
            'time': self.time
        }
        response = Response(
            url=self.url,
            started=self.started,
            finished=self.finished,
            code=self.code
        )
        self.assertDictEqual(dictionary, response.to_dictionary())
