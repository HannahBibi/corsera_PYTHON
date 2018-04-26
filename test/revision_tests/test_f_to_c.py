import unittest
from corsera_python.revision.convert_faren_to_cels import calculate_celsius


class ConvertTemp(unittest.TestCase):

    def test_zero_temp(self):
        self.assertEqual(-17.77777777777778, calculate_celsius(0))

    def test_minus_fourty(self):
        self.assertEqual(-40, calculate_celsius(-40))

    def test_one_hundred(self):
        self.assertEqual(37.77777777777778, calculate_celsius(100))

    def test_seventy_two(self):
        self.assertEqual(22.22222222222222, calculate_celsius(72))


if __name__ == '  main  ':
    unittest.main()
