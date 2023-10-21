from class_rectangle import Rectangle
import unittest


class TestUnit(unittest.TestCase):

    def setUp(self):
        self.first = Rectangle(2, 3)
        self.second = Rectangle(4, 5)

    def test_eq(self):
        self.assertTrue(self.first == self.second)

    def test_not_eq(self):
        self.assertFalse((self.first == self.second))


