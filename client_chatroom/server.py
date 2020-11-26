import socket
import threading
import time

HOST = socket.gethostbyname(socket.gethostname())
PORT = 15557
ADDR = (HOST, PORT)
TIMEOUT = 5 # seconds before the server closes
MAX_PEOPLE = 30

def chat(client, addr):
    pass


def run_server():
        global MAX_PEOPLE
        print(f"[SEARCHING FOR CLIENT...]")
        server.listen(MAX_PEOPLE)
        
        while True:
            global people
            client, addr = server.accept()
            print(f"[CONNECTED SUCCESSFULLY TO {addr}")
            thread = threading.Thread(target=chat, args=(client, addr))
            thread.start()
            people += 1
            print(f"there are now {people} people in the chatroom")
            if people > 10:
                break
        server.close()



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"[BINDING SERVER...]")
server.bind(ADDR)
people = 0
run_server()