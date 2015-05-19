from performance_testing import errors


class Config:
    def check_valid(self):
        attributes = ['host', 'requests_count', 'clients_count', 'requests']
        for attribute in attributes:
            try:
                getattr(self, attribute)
            except AttributeError as ex:
                raise errors.ConfigError(config_key=attributes)

    def url(self, url):
        return self.host + url


class Request:
    def __init__(self, url, type='GET', data=''):
        self.url = url
        self.type = type
        self.data = data
