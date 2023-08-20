import socket
from select import select

tasks = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostbyname_ex(socket.gethostname())[-1][0])
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 5001))
server.listen()


def accepting(server):
        client, addr = server.accept()
        print(f"Есть подключение {addr[0]}:{addr[1]}")
        tasks.append(client)


def send_message(client):
        response = client.recv(1024).decode()
        if response:
            print('msg:', response)
        else:
            client.close()
            tasks.remove(client)


def event_loop():
    while True:
        ready_to_read, _, _ = select(tasks, [], [])
        for sock in ready_to_read:
            if sock is server:
                accepting(server=sock)
            else:
                send_message(client=sock)


tasks.append(server)
event_loop()