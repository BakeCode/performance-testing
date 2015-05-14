import unittest
import os
from performance_testing.command_line import Tool
from performance_testing.errors import ConfigFileError, ConfigKeyError


class CommandLineToolTest(unittest.TestCase):
    def setUp(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.config = os.path.join(self.current_directory, 'assets/test_config.yml')
        self.result_directory = os.path.join(self.current_directory, 'assets/test_result')
        if os.path.exists(self.result_directory):
            os.removedirs(self.result_directory)
        self.tool = Tool(self.config, result_directory=self.result_directory)

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

    def test_read_config(self):
        with self.assertRaises(ConfigFileError) as ex:
            self.tool.read_config(config='foo/bar')
        self.assertEquals(ex.exception.message, 'Config file not exists "foo/bar".')

        with self.assertRaises(ConfigKeyError) as ex:
            self.tool.read_config(config=os.path.join(self.current_directory, 'assets/test_no_host_config.yml'))
        self.assertEquals(ex.exception.message, 'Config with key "host" not set.')

        with self.assertRaises(ConfigKeyError) as ex:
            self.tool.read_config(config=os.path.join(self.current_directory, 'assets/test_no_requests_config.yml'))
        self.assertEquals(ex.exception.message, 'Config with key "requests" not set.')

        with self.assertRaises(ConfigKeyError) as ex:
            self.tool.read_config(config=os.path.join(self.current_directory, 'assets/test_no_clients_config.yml'))
        self.assertEquals(ex.exception.message, 'Config with key "clients" not set.')

        with self.assertRaises(ConfigKeyError) as ex:
            self.tool.read_config(config=os.path.join(self.current_directory, 'assets/test_no_time_config.yml'))
        self.assertEquals(ex.exception.message, 'Config with key "time" not set.')

        with self.assertRaises(ConfigKeyError) as ex:
            self.tool.read_config(config=os.path.join(self.current_directory, 'assets/test_no_urls_config.yml'))
        self.assertEquals(ex.exception.message, 'Config with key "urls" not set.')
        
