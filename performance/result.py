from performance.web import Response


class Result:
    def __init__(self, result_file):
        self.result_file = result_file
        # create file

    def add_response(self, response):
        # check if response is Response object
        # append to data file
        pass


class Chart:
    def __init__(self, file_path):
        self.file_path = file_path

    def html(self, result_data):
        # fetch data and write in html file
        pass
