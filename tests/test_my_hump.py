from myapp.my_func import my_func
import unittest


class MyTestCase(unittest.TestCase):
    def test_my_func(self):
        self.assertEqual(my_func(), "Hallo Welt!")
