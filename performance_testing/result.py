import os
from datetime import datetime
from time import time


class Result:
    def __init__(self, directory):
        date = datetime.fromtimestamp(time())
        self.file = File(directory, date.strftime('%Y-%m-%d_%H-%M-%S'))


class File:
    def __init__(self, directory, name):
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.path = os.path.join(directory, name)
        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def write_line(self, text):
        stream = open(self.path, 'a')
        stream.write('%s\n' % text)
        stream.close()
