from myapp.my_func import my_func, my_other_func
import unittest


class MyTestCase(unittest.TestCase):
    def test_my_func(self):
        self.assertEqual("Hallo Welt!", "Hallo Welt!")

    def test_my_other_func(self):
        self.assertEqual("Hallo Welt!", "Hallo Welt!")


