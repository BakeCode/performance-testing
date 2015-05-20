class Request:
    GET = 'get'
    POST = 'post'

    def __init__(self, url, type, data=None):
        self.url = url
        self.type = type
        self.data = data
