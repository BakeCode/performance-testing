import unittest
from performance_testing.result import Result, File
import os
import shutil


class ResultTestCase(unittest.TestCase):
    def setUp(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.result_directory = os.path.join(self.current_directory, 'assets/test_result')

    def test_result_init(self):
        if os.path.exists(self.result_directory):
            shutil.rmtree(self.result_directory)
        self.assertFalse(os.path.exists(self.result_directory))
        result = Result(directory=self.result_directory)
        self.assertTrue(os.path.exists(self.result_directory))
        self.assertTrue(os.path.exists(result.file.path))
