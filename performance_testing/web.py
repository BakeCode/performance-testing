import requests
from time import time


class TimeRequest:
    @staticmethod
    def get(url):
        start = time()
        response = requests.get(url)
        end = time()
        return end - start

    @staticmethod
    def post(url, data):
        start = time()
        response = requests.post(url, data=data)
        end = time()
        return end - start
