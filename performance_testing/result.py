import os
from datetime import datetime


class Result:
    def __init__(self, directory):
        date = datetime.fromtimestamp(time())
        name = '%d-%d-%d_%d-%d-%d' % (datetime.year,
                                      datetime.month,
                                      datetime.day,
                                      datetime.hour,
                                      datetime.minute,
                                      datetime.second)
        self.file = File(directory, name)


class File:
    def __init__(self, directory, name):
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.path = os.path.join(directory, name)
        if not os.path.exists(self.path):
            open(self.path, 'a').close()

    def write_line(self, text):
        stream = open(self.path, 'w')
        stream.write('%s\n' % text)
        stream.close()
