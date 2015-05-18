import unittest
import os
import shutil
from performance_testing.command_line import Tool
from performance_testing.result import Result
from performance_testing.config import Config
from performance_testing.errors import ConfigFileError, ConfigKeyError


class CommandLineToolTest(unittest.TestCase):
    def setUp(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.config = os.path.join(self.current_directory, 'assets/test_config.yml')
        self.result_directory = os.path.join(self.current_directory, 'assets/test_result')

    def test_init(self):
        tool = Tool(config=self.config, result_directory=self.result_directory)
        self.assertIsInstance(tool.config, Config)
        self.assertIsInstance(tool.result, Result)
