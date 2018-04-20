import unittest
from corsera_python.module3.SumSocketAssignment import assignment1, assignment2

def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


def get_file_contents(fn):
    f = get_file_path(fn)
    fh = open(f)
    data = fh.read()
    fh.close()
    return data


def strip_cr_lf(s): return s.replace("\n", "").replace("\r", "")

class SumAssignment(unittest.TestCase):

    def test_given_sum(self):
        r = assignment1('http://py4e-data.dr-chuck.net/comments_42.html')
        print(r)

    def test_ending_in_23(self):
        w = assignment1('http://py4e-data.dr-chuck.net/comments_86513.html')
        print(w)

    def test_fikret(self):
        rng = 4
        pos = 2
        actual = assignment2('http://py4e-data.dr-chuck.net/known_by_Fikret.html', rng, pos)
        print(actual)

    def test_kristofer(self):
        rng = 7
        pos = 17
        actual = assignment2('http://py4e-data.dr-chuck.net/known_by_Kristofer.html', rng, pos)
        print(actual)




if __name__ == '__main__':
    unittest.main()