import unittest
from corsera_python.PythonMax import max


class PythonMax(unittest.TestCase):

    def test_should_find_74(self):
        self.assertEqual(74, max ([3, 41, 27, 74, 15]))

    def test_empty(self):
        self.assertEqual(0, max([]))


if __name__ == '  main  ':
    unittest.main()