import unittest
from performance.routine import Config


class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.host = 'http://www.google.com'

    def test_init(self):
        config = Config(host=self.host)
        self.assertEqual(self.host, config.host)
        self.assertEqual([], config.requests)
