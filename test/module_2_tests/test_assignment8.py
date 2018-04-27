import unittest
from coursera_python.module2.assignment8 import extract_float

class assignmnt8(unittest.TestCase):

    def test_extraction_one(self):
        t = "X-DSPAM-Confidence:    0.8475"
        self.assertEqual(0.8475, extract_float(t))

if __name__ == '  main  ':
    unittest.main()