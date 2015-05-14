import os
import yaml


class Tool:
    def __init__(self, config='config.yml', result_directory='result'):
        self.read_config(config)
        self.create_result_directory(result_directory)

    def read_config(self, config):
        try:
            config_stream = open(config, 'r')
            config_data = yaml.load(config_stream)
            self.host = config_data['host']
            self.requests = config_data['requests']
            self.clients = config_data['clients']
            self.time = config_data['time']
            self.urls = config_data['urls']
        except KeyError, ex:
            raise ex
        except IOError:
            raise IOError('Config file error "%s".' % config)

    def create_result_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.result_directory = directory

    def run(self):
        pass
