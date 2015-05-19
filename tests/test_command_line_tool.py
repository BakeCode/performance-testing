import unittest
import os
from performance_testing.command_line import Tool
from performance_testing.result import Result
from performance_testing.config import Config
import config


class CommandLineToolTest(unittest.TestCase):
    def setUp(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.result_directory = os.path.join(self.current_directory, 'assets/test_result')

    def test_init(self):
        tool = Tool(config=config.CONFIG, result_directory=self.result_directory)
        self.assertIsInstance(tool.config, Config)
        self.assertIsInstance(tool.result, Result)
