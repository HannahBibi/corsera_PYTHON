import unittest
from corsera_python.PythonEvens import evens

class PythonEvens(unittest.TestCase):

    def test_evens_one(self):
        self.assertEqual(3, evens([0, 1, 2, 3, 4]))

    def test_empty(self):
        self.assertEqual(0, evens([]))

    def test_negatives(self):
        self.assertEqual(3, evens([0, -1, -2, -3, -4]))


if __name__ == '  main  ':
    unittest.main()
