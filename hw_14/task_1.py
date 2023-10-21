from class_employee import *
import unittest


class TestUnit(unittest.TestCase):

    def setUp(self):
        self.first = Employee('Alex', 'Potter', 'Shprehter', 24, 123456)
        self.another_first = Employee('Alex', 'Potter', 'Shprehter', 24, 123456)
        self.second = Employee('Andrew', 'ofofofof', 'qwerty', 22, 123656)

    def test_is(self):
        self.assertFalse(self.first is self.another_first)

    def test_eq(self):
        self.assertTrue(self.first == self.another_first)

    def test_not_eq(self):
        self.assertFalse(self.first == self.second)

    def test_exist(self):
        self.assertRaises(Exception, Employee, ('rnd_name', 'rnd_surname', 'rnd_patronymic', 0, 123))


if __name__ == '__main__':
    unittest.main(verbosity=True)
