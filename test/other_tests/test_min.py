import unittest
from corsera_python.other.PythonMin import minimum


class PythonMin(unittest.TestCase):

    def test_should_find_3(self):
        self.assertEqual(3, minimum([3, 41, 27, 74, 15]))

    def test_empty(self):
        self.assertEqual(None, minimum([]))


if __name__ == '  main  ':
    unittest.main()
