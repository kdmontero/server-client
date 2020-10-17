import socket

FORMAT = 'utf-8'
PORT = 5562
HOST = '192.168.22.19'
SERVER_ADDR = (HOST, PORT)
DISCONNECT_MSG = 'exit()'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"[CONNECTING TO SERVER...]")
client.connect(SERVER_ADDR)
print(f"[YOU ARE NOW CONNECTED TO SERVER] {HOST}")
connected = True
while connected:
    msg = bytes(input("Enter your message: "), FORMAT)
    client.send(msg)
    response = client.recv(1024).decode(FORMAT)
    print(f"echo_server: {response}")
    if response == DISCONNECT_MSG:
        connected = False
client.close()
print(f"[DISCONNECTED...]")