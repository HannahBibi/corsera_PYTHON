import unittest
from unittest.mock import MagicMock
from coursera_python.module3.SocketAssignment import assignment2


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


class FindNameAssignment(unittest.TestCase):

    def test_mock_call(self):
        known_html = get_file_contents('known_by_Fikret.html')
        url = 'Nonsense'
        urllib_mock = MagicMock()
        urllib_mock.request.urlopen(url).read.side_effect = [known_html]

        rng = 1
        pos = 2
        actual = assignment2(urllib_mock, url, rng, pos)
        self.assertEqual('Montgomery', actual)


    @unittest.skip('Skipped because this hits the internet')
    def test_fikret(self):
        rng = 4
        pos = 2
        actual = assignment2('http://py4e-data.dr-chuck.net/known_by_Fikret.html', rng, pos)
        print(actual)

    @unittest.skip('Skipped because this hits the internet')
    def test_kristofer(self):
        rng = 7
        pos = 17
        actual = assignment2('http://py4e-data.dr-chuck.net/known_by_Kristofer.html', rng, pos)
        print(actual)


if __name__ == '__main__':
    unittest.main()
