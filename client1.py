import socket

HOST = '192.168.1.171'
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    client.send(input("Введите сообщение: ").encode())



