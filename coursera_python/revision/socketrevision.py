import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input()
sock.connect((url, 80))
cmd = 'GET' + url + '\r\n\r\n'.encode()
sock.send(cmd)

while True:
    data = sock.recv(100)
    if len(data) < 1:
        break
    print(data.decode(), end='')

sock.close()
