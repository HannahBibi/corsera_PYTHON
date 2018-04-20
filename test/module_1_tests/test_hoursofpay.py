import unittest
from corsera_python.module1.hoursofpay import calculate_pay

class HoursofPay(unittest.TestCase):

    def test_calculate_pay(self):
        self.assertEqual(96.25, calculate_pay ("35", "2.75"))

    def test_rate_greater_than_0(self):
        self.assertEqual(0, calculate_pay("35", "-1"))

    def test_hours_cannot_be_negative(self):
        self.assertEqual(0, calculate_pay("-1", "2.75"))

if __name__ == '__main__':
    unittest.main()
