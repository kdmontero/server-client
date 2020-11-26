import socket
import time

PORT = 5571
HOST = socket.gethostbyname(socket.gethostname())
SERVER_ADDR = (HOST, PORT)
FORMAT = 'utf-8'
MSG_SIZE = 1024
DISCONNECT_MSG = 'exit()'
TIMEOUT = 5

def run_server():
    server.listen()
    print(f"[FINDING CONNECTIONS]...")
    client, addr = server.accept()
    print(f"[CONNECTED SUCCESSFULLY] {addr[0]}")
    echo_client(client, addr)


def send_msg(message, client): # message --> string
    global FORMAT
    msg = message.encode(FORMAT)
    client.send(msg)


def receive_msg(client):
    global MSG_SIZE
    global FORMAT
    msg_string = client.recv(MSG_SIZE).decode(FORMAT)
    return msg_string


def echo_client(client, addr):
    connected = True
    while connected:
        print(f"[WAITING FOR INPUT...]")
        msg_string = receive_msg(client)
        if msg_string == DISCONNECT_MSG:
            connected = False
        print(f"[MESSAGE RECEIVED:] \n{msg_string}")
        send_msg(msg_string, client)

    client.close()
    print(f"[DISCONNECTED...] {addr[0]}")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"[BINDING SERVER]... {HOST}")
server.bind(SERVER_ADDR)
run_server()