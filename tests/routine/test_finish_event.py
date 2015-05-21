import unittest
from performance.routine import FinishEvent


class FinishEventTestCase(unittest.TestCase):
    def test_init(self):
        event = FinishEvent()
        self.assertEqual(0, event.finished)

    def test_finish(self):
        event = FinishEvent()
        event.finish()
        self.assertEqual(1, event.finished)
        event.finish()
        self.assertEqual(2, event.finished)
        event.finish()
        self.assertEqual(3, event.finished)
