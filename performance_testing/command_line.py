import os
import yaml
from performance_testing.errors import ConfigFileError, ConfigKeyError
from performance_testing import web
from performance_testing.config import Config
from performance_testing.result import Result


class Tool:
    def __init__(self, config='config.yml', result_directory='result'):
        self.config = Config(config_path=config)
        self.result = Result(result_directory)

    def start_testing(self):
        pass

    def run(self):
        print('Start tests ...')
        for url in self.config.urls:
            full_url = self.config.host + url
            self.result.file.write_line('URL: %s\n' % url)
            for i in range(0, self.config.requests):
                self.result.file.write_line('    %i - %.3f\n' % (i, web.request(full_url)))
        print('Finished tests!')
