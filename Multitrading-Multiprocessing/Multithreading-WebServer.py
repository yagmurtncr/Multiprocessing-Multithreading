import threading
import socket
import time

def handle_client_request(client_socket):
    print("Client connected")
    # İstemci isteğini işleme
    client_socket.send(b"HTTP/1.1 200 OK\r\n\r\nHello, World!")
    client_socket.close()
    print("Client disconnected")

# Ana sunucu döngüsü
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8080))
server_socket.listen(5)

print("Server is listening on port 8080...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")
    client_thread = threading.Thread(target=handle_client_request, args=(client_socket,))
    client_thread.start()