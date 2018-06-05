from coursera_python.other.SimpleSocketServer import start_socket_server
import sys

port = int(sys.argv[1])

print(f'Starting server on port {port}')

start_socket_server(port)
