import json


class Result:
    def __init__(self):
        self.results = {}

    def add_result(self, client, url, result):
        if client not in self.results:
            self.results[client] = {}
        if url not in self.results[client]:
            self.results[client][url] = []
        self.results[client][url].append(result)

    def write(self, result_file):
        stream = open(result_file, 'w')
        stream.write(json.dumps(self.results))
        stream.close()
