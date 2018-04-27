import unittest
from coursera_python.other.PythonSum import sum

class PythonSum(unittest.TestCase):

    def test_sum_one(self):
        self.assertEqual(6, sum([1, 2, 3]))

    def test_sum_two(self):
        self.assertEqual(73, sum([20, 50, 3]))

    def test_sum_three(self):
        self.assertEqual(7, sum([1, 6]))

    def test_empty(self):
        self.assertEqual(0, sum([]))


if __name__ == '  main  ':
    unittest.main()