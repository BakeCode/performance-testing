import unittest
import os
from performance_testing.config import Config
from performance_testing.errors import ConfigKeyError, ConfigFileError


class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.config_path = os.path.join(self.current_directory, 'assets/test_config.yml')

    def test_init(self):
        config = Config(config_path=self.config_path)
        self.assertEqual(config.host, 'http://www.example.com')
        self.assertEqual(config.host, 'http://www.example.com')
        self.assertEqual(config.requests, 100)
        self.assertEqual(config.clients, 2)
        self.assertEqual(config.time, 60)
        self.assertEqual(config.urls, ['/', '/about'])

    def test_read_config(self):
        with self.assertRaises(ConfigFileError) as ex:
            config = Config(config_path='foo/bar')
        self.assertEqual(ex.exception.message, 'Config file not exists "foo/bar".')

        config_path = os.path.join(self.current_directory, 'assets/test_no_host_config.yml')
        with self.assertRaises(ConfigKeyError) as ex:
            config = Config(config_path=config_path)
        self.assertEqual(ex.exception.message, 'Config with key "host" not set.')

        config_path = os.path.join(self.current_directory, 'assets/test_no_requests_config.yml')
        with self.assertRaises(ConfigKeyError) as ex:
            config = Config(config_path=config_path)
        self.assertEqual(ex.exception.message, 'Config with key "requests" not set.')

        config_path = os.path.join(self.current_directory, 'assets/test_no_clients_config.yml')
        with self.assertRaises(ConfigKeyError) as ex:
            config = Config(config_path=config_path)
        self.assertEqual(ex.exception.message, 'Config with key "clients" not set.')

        config_path = os.path.join(self.current_directory, 'assets/test_no_time_config.yml')
        with self.assertRaises(ConfigKeyError) as ex:
            config = Config(config_path=config_path)
        self.assertEqual(ex.exception.message, 'Config with key "time" not set.')

        config_path = os.path.join(self.current_directory, 'assets/test_no_urls_config.yml')
        with self.assertRaises(ConfigKeyError) as ex:
            config = Config(config_path=config_path)
        self.assertEqual(ex.exception.message, 'Config with key "urls" not set.')
