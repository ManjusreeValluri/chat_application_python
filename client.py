import socket
import threading

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(f"\nServer: {message}")
            else:
                break
        except:
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5560))

thread = threading.Thread(target=receive_messages, args=(client,))
thread.start()

while True:
    msg = input("You: ")
    client.send(msg.encode())
