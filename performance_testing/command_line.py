import os
import yaml
from performance_testing.errors import ConfigFileError, ConfigKeyError
from performance_testing import web
from datetime import datetime as date
from time import time


class Tool:
    def __init__(self, config='config.yml', result_directory='result'):
        self.read_config(config_file=config)
        self.create_result_file(directory=result_directory)

    def read_config(self, config_file):
        try:
            config_stream = open(config_file, 'r')
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
            raise ConfigFileError(config_file)

    def create_result_file(self, directory):
        datetime = date.fromtimestamp(time())
        file_name = '%d-%d-%d_%d-%d-%d' % (datetime.year,
                                           datetime.month,
                                           datetime.day,
                                           datetime.hour,
                                           datetime.minute,
                                           datetime.second)
        file_path = os.path.join(directory, file_name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        open(file_path, 'a').close()
        self.result_file = file_path

    def start_testing(self):
        pass

    def run(self):
        file_stream = open(self.result_file, 'w')
        print('Start tests ...')
        for url in self.urls:
            full_url = self.host + url
            file_stream.write('URL: %s\n' % url)
            for i in range(0, self.requests):
                file_stream.write('    %i - %.3f\n' % (i, web.request(full_url)))
        print('Finished tests!')
