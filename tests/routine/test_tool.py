import unittest
from performance.routine import Tool, Config
from performance.web import Request
from io import StringIO
import sys
from threading import Thread
import _thread
import time


class ToolTestCase(unittest.TestCase):
    def setUp(self):
        self.host = 'http://www.google.com'
        self.requests = []
        self.requests.append(Request(url='/'))
        self.requests.append(Request(url='/about'))

    def test_init(self):
        config = Config(host=self.host)
        tool = Tool(config=config)
        self.assertEqual(config, tool.config)
        with self.assertRaises(TypeError) as error:
            tool = Tool(config='invalid_config')
        self.assertEqual('No performance.routine.Config object', error.exception.__str__())

    def test_run(self):
        config = Config(host=self.host, clients_count=2)
        print_results = StringIO()
        sys.stdout = print_results
        tool = Tool(config=config)
        tool.run()
        self.assertEqual(' > Invalid configuration\n', print_results.getvalue())
        print_results.close()
        print_results = StringIO()
        sys.stdout = print_results
        config.add_request(self.requests[0])
        config.add_request(self.requests[1])
        tool = Tool(config=config)
        tool.run()
        self.assertRegexpMatches(print_results.getvalue(), ' > Started tests\\n > Stop tests with CTRL-C\\n( > Finished a client\\n){2} > Finished 40 tests in [0-9]{1,10}\.[0-9]{2} seconds\\n')

    def test_run_interrupt(self):
        config = Config(host=self.host, clients_count=2)
        print_results = StringIO()
        sys.stdout = print_results
        config.add_request(self.requests[0])
        config.add_request(self.requests[1])
        tool = Tool(config=config)
        thread = Thread(target=interrupt)
        thread.start()
        tool.run()
        self.assertEqual(' > Started tests\n > Stop tests with CTRL-C\n > Interrupted a client\n > Interrupted a client\n > Exited with CTRL-C\n', print_results.getvalue())

def interrupt():
    time.sleep(1)
    _thread.interrupt_main()

