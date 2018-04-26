import unittest
from corsera_python.revision.convert_cels_to_faren import calculate_farenheit


class ConvertTemp(unittest.TestCase):

    def test_zero_temp(self):
        self.assertEqual(32, calculate_farenheit(0))

    def test_minus_fourty(self):
        self.assertEqual(-40, calculate_farenheit(-40))


if __name__ == '  main  ':
    unittest.main()
