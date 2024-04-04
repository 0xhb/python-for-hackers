import socket as s

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

host = "192.168.174.120"
port = 4444

client_socket.connect((host, port))

message = client_socket.recv(1024)

client_socket.close()
print(message.decode('ascii'))