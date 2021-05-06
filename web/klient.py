from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.0.101",12345))

while True:
    client.send(input().encode("utf-8"))