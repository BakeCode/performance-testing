import unittest
from performance.routine import Tool, Config


class ToolTestCase(unittest.TestCase):
    def setUp(self):
        self.host = 'http://www.google.com'
        self.config = Config(host=self.host)

    def test_init(self):
        tool = Tool(config=self.config)
        self.assertEqual(self.config, tool.config)
