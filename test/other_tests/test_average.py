import unittest
from coursera_python.other.PythonAverage import avg2

class PythonAverage(unittest.TestCase):

    def test_avg_one(self):
        self.assertEqual(5.5, avg2([4, 5, 6, 7]))


if __name__ == '  main  ':
    unittest.main()