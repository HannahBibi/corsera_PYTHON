def mock_one(sock, host, port, url):

    sock.connect((host, port))
    full_url = 'GET' + url + 'HTTP/1.0\r\n\r\n'
    sock.send(full_url.encode())

    data_str = ""
    while True:
        data = sock.recv(512)
        if (len(data) < 1):
            break
        data_str = data_str + data.decode()

    sock.close()
    return data_str
