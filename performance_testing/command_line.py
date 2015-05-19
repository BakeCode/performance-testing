from performance_testing.web import TimeRequest
from performance_testing.result import Result


class Tool:
    def __init__(self, config, result_directory='result'):
        self.config = config
        self.config.check_valid()
        self.result = Result(result_directory)

    def start_testing(self):
        pass

    def run(self):
        print('Start tests ...')
        for request in self.config.requests:
            full_url = self.config.url(request.url)
            self.result.file.write_line('URL: %s' % request.url)
            for i in range(0, self.config.requests_count):
                self.result.file.write_line('    %i - %.3f' % (i, TimeRequest.get(url=full_url)))
        print('Finished tests!')
