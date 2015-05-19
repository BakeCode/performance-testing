class Error(Exception):
    def __init__(self):
        self.message = 'bla'

    def __str__(self):
        return repr(self.message)


class ConfigError(Exception):
    def __init__(self, config_key):
        self.config_key = config_key
        self.message = 'Config with name "%s" not set.' % self.config_key
