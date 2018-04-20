import unittest
from unittest.mock import MagicMock
from corsera_python.module3.SocketGETAssignment import mock_one

class MockTests(unittest.TestCase):

    def test_make_mock(self):
        sock = MagicMock()
        sock.recv.side_effect = [b'Hello', b'']
        actual_result = mock_one(sock, 'Host', 95, 'http://abc.com')
        self.assertEqual('Hello', actual_result)

    def test_real_call(self):
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = mock_one(sock, 'data.pr4e.org', 80, 'http://data.pr4e.org/intro-short.txt')
        print(result)

    

if __name__ == '__main__':
    unittest.main()