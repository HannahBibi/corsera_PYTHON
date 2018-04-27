import unittest
from unittest.mock import MagicMock
from coursera_python.module3.module_three_assignment5 import crawl_data


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
        known_html = get_file_contents('comments_42.xml')
        url = 'Testing Mocks'
        url_mock = MagicMock()
        url_mock.request.urlopen(url).read.side_effect = [known_html]
        self.assertEqual(2553, crawl_data(url_mock, url))


    def test_mock_86515(self):
        known_html = get_file_contents('comments_86515.xml')
        url = 'Testing Mocks'
        url_mock = MagicMock()
        url_mock.request.urlopen(url).read.side_effect = [known_html]
        self.assertEqual(2499, crawl_data(url_mock, url))


if __name__ == '__main__':
    unittest.main()
