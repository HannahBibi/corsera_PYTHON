import unittest
from coursera_python.revision.convert_faren_to_cels import calculate_celsius


class ConvertTemp(unittest.TestCase):

    def test_zero_temp(self):
        self.assertEqual(-17.778, calculate_celsius(0))

    def test_for_a_negative_number(self):
        self.assertEqual(-40, calculate_celsius(-40))

    def test_for_a_positive_number(self):
        self.assertEqual(37.778, calculate_celsius(100))

    def test_for_three_decimal_places(self):
        self.assertEqual(-15.918, calculate_celsius(3.348))


if __name__ == '  main  ':
    unittest.main()
