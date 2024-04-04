
import socket as s

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

host = "127.0.0.1"
print(host)
port = 4444

server_socket.bind((host, port))

server_socket.listen(3)

while True:
    client_socket, address = server_socket.accept()
    print(f"Connection received from {str(address)}")

    message = "Hello! Thank you for connecting to my serer" + '\r\n'
    client_socket.send(message)

    client_socket.close()
