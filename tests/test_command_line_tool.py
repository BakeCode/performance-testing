import unittest
import os
from performance_testing.command_line import Tool


class CommandLineToolTest(unittest.TestCase):
    def setUp(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.config = os.path.join(self.current_directory, 'assets/test_config.yml')
        self.result_directory = os.path.join(self.current_directory, 'assets/test_result')
        if os.path.exists(self.result_directory):
            os.removedirs(self.result_directory)

    def test_init(self):
        tool = Tool(config=self.config, result_directory=self.result_directory)
        self.assertTrue(os.path.exists(self.result_directory))
        self.assertEquals(tool.result_directory,
                          os.path.join(self.current_directory,
                                       'assets/test_result'))
        self.assertEquals(tool.host, 'http://www.example.com')
        self.assertEquals(tool.requests, 100)
        self.assertEquals(tool.clients, 2)
        self.assertEquals(tool.time, 60)
        self.assertEquals(tool.urls, ['/', '/about'])
