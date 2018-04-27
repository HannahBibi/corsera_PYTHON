import unittest
from coursera_python.revision.convert_cels_to_faren import calculate_farenheit


class ConvertTemp(unittest.TestCase):

    def test_zero_temp(self):
        self.assertEqual(32, calculate_farenheit(0))

    def test_minus_fourty(self):
        self.assertEqual(-40, calculate_farenheit(-40))

    def test_positive_number(self):
        self.assertEqual(138.2, calculate_farenheit(59))

    def test_three_decimal_places(self):
        self.assertEqual(157.0226, calculate_farenheit(69.457))


if __name__ == '  main  ':
    unittest.main()
