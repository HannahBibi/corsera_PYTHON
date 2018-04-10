import unittest
from corsera_python.other.PythonCount import count

class PythonCount(unittest.TestCase):

    def test_count_one(self):
        self.assertEqual(3, count([1, 2, 3]))

    def test_empty(self):
        self.assertEqual(0, count([]))

if __name__ == '  main  ':
    unittest.main()