import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"\nClient: {message}")
            else:
                break
        except:
            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5560))
server.listen(1)
print("Server started... Waiting for connection.")

client_socket, addr = server.accept()
print(f"Connected with {addr}")

thread = threading.Thread(target=handle_client, args=(client_socket,))
thread.start()

while True:
    msg = input("You: ")
    client_socket.send(msg.encode())
