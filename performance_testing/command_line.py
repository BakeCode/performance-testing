import os
import yaml
from performance_testing.errors import ConfigFileError, ConfigKeyError
import web


class Tool:
    def __init__(self, config='config.yml', result_directory='result'):
        self.read_config(config)
        self.create_result_directory(result_directory)

    def read_config(self, config):
        try:
            config_stream = open(config, 'r')
            config_data = yaml.load(config_stream)
            config_stream.close()
            self.host = config_data['host']
            self.requests = config_data['requests']
            self.clients = config_data['clients']
            self.time = config_data['time']
            self.urls = config_data['urls']
        except KeyError as ex:
            raise ConfigKeyError(ex.args[0])
        except IOError:
            raise ConfigFileError(config)

    def create_result_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.result_directory = directory

    def run(self):
        print 'Run tests'
        for url in self.urls:
            full_url = self.host + url
            print 'URL: %s' % url
            for i in range(0, self.requests):
                print '%i - %.3f' % (i, web.request(full_url))
