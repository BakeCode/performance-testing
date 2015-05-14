import os
import yaml


class Tool:
    def __init__(self, config='config.yml', output_directory='result'):
        self.read_config(config)
        self.create_output_directory(output_directory)

    def read_config(self, config):
        config_stream = open(config, 'r')
        config_data = yaml.load(config_stream)
        self.host = config_data['host']
        self.requests = config_data['requests']
        self.clients = config_data['clients']
        self.time = config_data['time']
        self.urls = config_data['urls']

    def create_output_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def run(self):
        pass
