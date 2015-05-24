import unittest
from performance.routine import Tool, Config
from performance.web import Request
from threading import Thread
import _thread
import time
from nose.plugins.capture import Capture


class ToolTestCase(unittest.TestCase):
    def setUp(self):
        self.host = 'http://www.google.com'
        self.requests = []
        self.requests.append(Request(url='/'))
        self.requests.append(Request(url='/about'))
        self.capture = Capture()
        self.capture.begin()

    def test_init(self):
        config = Config(host=self.host)
        tool = Tool(config=config)
        self.assertEqual(config, tool.config)
        with self.assertRaises(TypeError) as error:
            tool = Tool(config='invalid_config')
        self.assertEqual('No performance.routine.Config object', error.exception.__str__())

    def test_run(self):
        config = Config(host=self.host, clients_count=2)
        tool = Tool(config=config)
        self.capture.beforeTest(test=None)
        tool.run()
        self.assertEqual(' > Invalid configuration\n', self.capture.buffer)
        self.capture.afterTest(test=None)
        config.add_request(self.requests[0])
        config.add_request(self.requests[1])
        tool = Tool(config=config)
        self.capture.beforeTest(test=None)
        tool.run()
        self.assertRegexpMatches(
            self.capture.buffer,
            ' > Started tests\n > Stop tests with CTRL-C\n( > Finished a client\n){2} > Finished 40 tests in [0-9]{1,4}\.[0-9]{2} seconds\n'
        )
        self.capture.afterTest(test=None)

    def test_run_interrupt(self):
        config = Config(host=self.host, clients_count=2)
        config.add_request(self.requests[0])
        config.add_request(self.requests[1])
        tool = Tool(config=config)
        thread = Thread(target=interrupt)
        thread.start()
        self.capture.beforeTest(test=None)
        tool.run()
        self.assertEqual(
            ' > Started tests\n > Stop tests with CTRL-C\n > Exited with CTRL-C\n',
            self.capture.buffer
        )
        self.capture.afterTest(test=None)

def interrupt():
    time.sleep(0.1)
    _thread.interrupt_main()
