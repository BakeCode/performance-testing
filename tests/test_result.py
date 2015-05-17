import unittest
from performance_testing.result import Result, File
import os
import shutil


class ResultTestCase(unittest.TestCase):
    def setUp(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.result_directory = os.path.join(self.current_directory, 'assets/test_result')
        self.test_file_name = 'foo_bar'
        self.test_file_path = os.path.join(self.result_directory, self.test_file_name)

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
        self.assertFalse(os.path.exists(self.result_directory))
        file = File(directory=self.result_directory, name=self.test_file_name)
        self.assertTrue(os.path.exists(self.result_directory))
        self.assertTrue(os.path.exists(self.test_file_path))

    def test_write_file(self):
        self.clear_result_dir()
        file = File(directory=self.result_directory, name=self.test_file_name)
        stream = open(self.test_file_path, 'r')
        self.assertEqual(stream.read(), '')
        stream.close()

        text = 'askld asjdjidjj saidj98e12ud0- asid902ur890a'
        file.write_line(text)
        stream = open(self.test_file_path, 'r')
        self.assertEqual(stream.read(), text + '\n')
        stream.close()

    def tearDown(self):
        self.clear_result_dir()
