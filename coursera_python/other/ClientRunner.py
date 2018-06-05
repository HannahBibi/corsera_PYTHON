from coursera_python.other.SimpleSocketServer import simple_server_client
import sys

host = sys.argv[1]
port = int(sys.argv[2])

simple_server_client(host, port)
