class Error(Exception):
    def __init__(self):
        self.message = ''

    def __str__(self):
        return repr(self.message)


class ConfigFileError(Exception):
    def __init__(self, file):
        self.file = file
        self.message = 'Config file not exists "%s".' % self.file


class ConfigKeyError(Exception):
    def __init__(self, key):
        self.key = key
        self.message = 'Config with key "%s" not set.' % self.key
