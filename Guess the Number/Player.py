import socket

PORT = 8081
IP = "127.0.0.1"

print(f"Connection to SERVER at {IP}, PORT: {PORT}")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.connect((IP,PORT))

s.send(str.encode(msg)
response = s.recv(2048).decode("utf-8")
s.close()

