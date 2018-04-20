import unittest
from corsera_python.module3.SumSocketAssignment import running_count

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
        r = running_count('http://py4e-data.dr-chuck.net/comments_42.html')
        print(r)

    def test_ending_in_23(self):
        w = running_count('http://py4e-data.dr-chuck.net/comments_86513.html')
        print(w)





if __name__ == '__main__':
    unittest.main()