import socket
import time

FORMAT = 'utf-8'
MSG_SIZE = 1024
PORT = 15557
HOST = '192.168.22.19'
SERVER_ADDR = (HOST, PORT)
DISCONNECT_MSG = 'exit()'


def send_msg(message, client): # message --> string
    global FORMAT
    msg = message.encode(FORMAT)
    client.send(msg)


def receive_msg(client):
    global MSG_SIZE
    global FORMAT
    msg_string = client.recv(MSG_SIZE).decode(FORMAT)
    return msg_string


def connect(server_address):
    host = server_address[0]
    print(f"[CONNECTING TO SERVER...]")
    client.connect(server_address)
    print(f"[YOU ARE NOW CONNECTED TO SERVER] {host}")


def echo_chat(client):
    global DISCONNECT_MSG
    connected = True
    while connected:
        msg = input("Enter your message (type 'exit()' to disconnect): ")
        if not msg:
            continue
        send_msg(msg, client)
        response = receive_msg(client)
        if response == DISCONNECT_MSG:
            connected = False
            response = 'Thank you for using echo server!'
        print(f"echo_server: {response}")
    client.close()
    print(f"[DISCONNECTED...]")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect(SERVER_ADDR)
time.sleep(15)