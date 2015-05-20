import unittest
from performance.routine import Tool, Config


class ToolTestCase(unittest.TestCase):
    def setUp(self):
        self.host = 'http://www.google.com'
        self.config = Config(host=self.host)

    def test_init(self):
        tool = Tool(config=self.config)
        self.assertEqual(self.config, tool.config)
        with self.assertRaises(TypeError) as error:
            tool = Tool(config='invalid_config')
        self.assertEqual('No performance.routine.Config object', error.exception.message)
