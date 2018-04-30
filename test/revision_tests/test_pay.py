import unittest
from coursera_python.revision.revision_pay_rate import normal_pay, overtime_pay, total_pay


class CalculateNormalPay(unittest.TestCase):

    def test_with_no_overtime(self):
        self.assertEqual(400, normal_pay(40, 10))

    def test_with_minus_hours(self):
        self.assertEqual(-400, normal_pay(-40, 10))

    def test_with_minus_rate(self):
        self.assertEqual(-400, normal_pay(40, -10))

    def test_with_zero_hours(self):
        self.assertEqual(0, normal_pay(0, 10))

    def test_with_zero_rate(self):
        self.assertEqual(0, normal_pay(10, 0))

    def test_with_zero(self):
        self.assertEqual(0, normal_pay(0, 0))

    def test_with_less_than_fourty(self):
        self.assertEqual(350, normal_pay(35, 10))

    def test_greater_than_fourty(self):
        self.assertEqual(400, normal_pay(45, 10))

    def test_diff_rate_greater_than_fourty(self):
        self.assertEqual(376.0, normal_pay(89, 9.4))


class CalculateOvertimePay(unittest.TestCase):

    def test_with_fourty_five(self):
        self.assertEqual(75.0, overtime_pay(45, 10))

    def test_with_zero(self):
        self.assertEqual(0, overtime_pay(0, 0))

    def test_with_minus_rate(self):
        self.assertEqual(-60.0, overtime_pay(45, -8))

    def test_with_zero_hours(self):
        self.assertEqual(0, overtime_pay(0, 10))

    def test_with_less_than_fourty_five(self):
        self.assertEqual(0, overtime_pay(24, 10))


class ClassTotalPay(unittest.TestCase):

    def test_with_fourty_five(self):
        self.assertEqual(475.0, total_pay(45, 10))

    def test_with_zero(self):
        self.assertEqual(0, total_pay(0, 0))

    def test_with_minus_hours(self):
        self.assertEqual(-450, total_pay(-45, 10))

    def test_with_minus_rate(self):
        self.assertEqual(-475.0, total_pay(45, -10))

    def test_with_less_than_fourty_five(self):
        self.assertEqual(240, total_pay(24, 10))

    def test_with_more_than_fourty_five(self):
        self.assertEqual(3400.0, total_pay(240, 10))


if __name__ == '  main  ':
    unittest.main()
