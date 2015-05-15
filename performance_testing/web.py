import requests
import time


def request(url):
    start = time.time()
    response = requests.get(url)
    end = time.time()
    return end - start
