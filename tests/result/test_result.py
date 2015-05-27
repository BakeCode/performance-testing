import unittest
from performance.result import Result


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
