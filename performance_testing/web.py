import requests
from time import time


def request(url):
    start = time()
    response = requests.get(url)
    end = time()
    return end - start
