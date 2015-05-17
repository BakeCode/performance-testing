import unittest
from performance_testing.result import Result, File
import os
import shutil


class ResultTestCase(unittest.TestCase):
    def setUp(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.result_directory = os.path.join(self.current_directory, 'assets/test_result')

    def clear_result_dir(self):
        if os.path.exists(self.result_directory):
            shutil.rmtree(self.result_directory)

    def test_result_init(self):
        self.clear_result_dir()
        self.assertFalse(os.path.exists(self.result_directory))
        result = Result(directory=self.result_directory)
        self.assertTrue(result.file.path)

    def test_file_init(self):
        self.clear_result_dir()
        file_name = 'foo_bar'
        self.assertFalse(os.path.exists(self.result_directory))
        file = File(directory=self.result_directory, name=file_name)
        self.assertTrue(os.path.exists(self.result_directory))
        self.assertTrue(os.path.exists(os.path.join(self.result_directory, file_name)))

    def tear_down(self):
        self.clear_result_dir()
