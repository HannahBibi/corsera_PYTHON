import unittest
from unittest.mock import MagicMock
from corsera_python.module3.SocketAssignment import assignment1


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


class SumAssignmentTests(unittest.TestCase):

    def test_mock_call(self):

        known_html = get_file_contents('comments_42.html')

        ulib_mock = MagicMock()
        url = 'This is a nonsense url'
        ulib_mock.request.urlopen(url).read.side_effect = [known_html]

        actual_result = assignment1(ulib_mock, url)
        self.assertEqual(2553, actual_result)


    @unittest.skip('Skipped because this hits the internet')
    def test_real_call(self):
        import urllib
        url = 'http://py4e-data.dr-chuck.net/comments_42.html'
        actual_result = assignment1(urllib, url)
        self.assertEqual(2553, actual_result)


    @unittest.skip('Skipped because this hits the internet')
    def test_ending_in_23(self):
        w = assignment1('http://py4e-data.dr-chuck.net/comments_86513.html')
        print(w)




if __name__ == '__main__':
    unittest.main()
