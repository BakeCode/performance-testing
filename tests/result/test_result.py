import unittest
from performance.result import Result
import json


class ResultTestCase(unittest.TestCase):
    def test_init(self):
        result = Result()
        self.assertDictEqual({}, result.results)

    def test_add_result(self):
        result = Result()
        result.add_result(client='client_0', url='/about', result=0.23)
        self.assertDictEqual({
            'client_0': {
                '/about': [0.23]
            }
        }, result.results)
        result.add_result(client='client_0', url='/about', result=0.523)
        self.assertDictEqual({
            'client_0': {
                '/about': [0.23, 0.523]
            }
        }, result.results)

    def test_write(self):
        result = Result()
        result.add_result(client='client_0', url='/about', result=0.23)
        result.add_result(client='client_0', url='/about', result=0.5213)
        result.write(result_file='result/test_file.json')
        stream = open('result/test_file.json', 'r')
        text = stream.read()
        stream.close()
        self.assertDictEqual({
            'client_0': {
                '/about': [0.23, 0.5213]
            }
        }, json.loads(text))
