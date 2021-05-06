from socket import *
from icecream import ic

server = socket(AF_INET, SOCK_STREAM)
server.bind(("192.168.0.101", 55000))
server.listen()

while True:
    connection, adres = server.accept()
    print('Server connected', adres)
    while True:
        data = connection.recv(1024)
        check = data.decode("utf-8").lower()
        ic(check)
        if not data: break
        connection.send(b'accept->' + data)
    connection.close()
