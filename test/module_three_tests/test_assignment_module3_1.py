import unittest
from corsera_python.module3.module_three_assignment1 import extract_sum


def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


class Assignment1Module3(unittest.TestCase):

    def test_sum_42(self):
        regex_sum_42 = get_file_path('regex_sum_42.txt')
        self.assertEqual(445833, extract_sum(regex_sum_42))

    def test_sum_86511(self):
        regex_sum_86511 = get_file_path('regex_sum_86511.txt')
        self.assertEqual(456126, extract_sum(regex_sum_86511))


if __name__ == '  main  ':
    unittest.main()
