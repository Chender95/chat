import socket

HOST = '0.0.0.0'
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostbyname_ex(socket.gethostname())[-1][0])
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

while True:
    client, addr = server.accept()
    print(client, "client")
    print(f"Есть подключение {addr[0]}:{addr[1]}")
    while True:
        response = client.recv(1024).decode()
        if not response:
            break
        else:
            print('msg:', response)
    client.close()