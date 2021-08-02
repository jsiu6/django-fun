import socket

info = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    link = input('Enter link: ')
    info.connect((link, 80))

    command = 'GET ' + link + ' HTTP/1.0\r\n\r\n'
    info.send(command.encode())

    while True:
        data = info.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')
except Exception as ex:
    print('Error: ' + str(ex))
info.close()
