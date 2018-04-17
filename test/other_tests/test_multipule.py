import unittest
from corsera_python.other.PythonMultiple import multiply_list_items


class PythonMultiple(unittest.TestCase):

    def test_multiply_twos(self):
        self.assertEqual(4, multiply_list_items([2, 2]))

    def test_multiply_one_int(self):
        self.assertEqual(3, multiply_list_items([3]))

    def test_multiply_empty(self):
        self.assertEqual(None, multiply_list_items([]))

    def test_multipling_zero(self):
        self.assertEqual(0, multiply_list_items([2, 0]))

    def test_multiply_minus(self):
        self.assertEqual(4, multiply_list_items([-2, -2]))

    def test_multiply_minus_and_positive(self):
        self.assertEqual(-8, multiply_list_items([2, -4]))


if __name__ == '  main  ':
    unittest.main()
