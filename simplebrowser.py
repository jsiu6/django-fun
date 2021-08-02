import socket

info = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
info.connect(('data.pr4e.org', 80))
command = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
info.send(command)

while True:
    data = info.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

info.close()
