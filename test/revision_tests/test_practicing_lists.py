import unittest
from coursera_python.revision.PracticingWithLists import chop


class TestingChop(unittest.TestCase):

    def testing_a_list(self):
        l = [1, 2, 3]
        chop(l)
        self.assertEqual(l, [2])


if __name__ == '  main  ':
    unittest.main
