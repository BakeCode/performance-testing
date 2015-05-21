import unittest
from performance.web import RequestTypeError


class RequestTypeErrorTestCase(unittest.TestCase):
    def test_init(self):
        type = 'get'
        error = RequestTypeError(type)
        self.assertEqual(type, error.type)

    def test_to_string(self):
        type = 'get'
        error = RequestTypeError(type)
        self.assertEqual('Invalid request type "%s"' % type, error.__str__())