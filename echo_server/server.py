import socket

PORT = 5562
HOST = socket.gethostbyname(socket.gethostname())
SERVER_ADDR = (HOST, PORT)
FORMAT = 'utf-8'
HEADER = 16
DISCONNECT_MSG = 'exit()'

def run_server():
    server.listen()
    print(f"[FINDING CONNECTIONS]...")
    client, addr = server.accept()
    print(f"[CONNECTED SUCCESSFULLY] {addr[0]}")
    echo_client(client, addr)

def echo_client(client, addr):
    connected = True
    while connected:
        print(f"[WAITING FOR INPUT...]")
        # msg_length = int(client.recv(HEADER).decode(FORMAT))
        msg = client.recv(1024)
        msg_string = msg.decode(FORMAT)
        if msg_string == DISCONNECT_MSG:
            connected = False
        print(f"[MESSAGE RECEIVED:] \n{msg_string}")
        client.send(msg)
    client.close()
    print(f"[DISCONNECTED...] {addr[0]}")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"[BINDING SERVER]... {HOST}")
server.bind(SERVER_ADDR)
run_server()