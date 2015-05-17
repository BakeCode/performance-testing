import os
import yaml
from performance_testing import errors


class Config:
    def __init__(self, config_path='config.yml'):
        try:
            stream = open(config_path, 'r')
            config_data = yaml.load(stream)
            stream.close()
            self.host = config_data['host']
            self.requests = config_data['requests']
            self.clients = config_data['clients']
            self.time = config_data['time']
            self.urls = config_data['urls']
        except KeyError as ex:
            raise errors.ConfigKeyError(ex.args[0])
        except IOError:
            raise errors.ConfigFileError(config_path)
