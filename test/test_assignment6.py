import unittest
from corsera_python.week6assignment import normal_pay, overtime_hrs, overtime_pay, computepay


class week6assignment(unittest.TestCase):

    def test_normal_pay(self):
        self.assertEqual(420, normal_pay(45, 10.5))

    def test_overtime_hrs(self):
        self.assertEqual(5, overtime_hrs(45))

    def test_overtime_pay(self):
        self.assertEqual(78.75, overtime_pay(45, 10.5))

    def test_computepay(self):
        self.assertEqual(498.75, computepay(45, 10.5))

    def test_zero_hours(self):
        self.assertEqual(0, computepay(0, 10.5))

    def test_zero_rate(self):
        self.assertEqual(0, computepay(45, 0))


if __name__ == '__main__':
    unittest.main()

