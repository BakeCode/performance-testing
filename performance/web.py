class Request:
    GET = 'get'
    POST = 'post'

    def __init__(self, url, type, data=None):
        self.url = url
        self.type = type
        self.data = data


class RequestData:
    def __init__(self, data=None):
        self.data = data

    def for_type(self, type=Request.GET):
        if type is Request.GET:
            return data
