import socket
import termcolor
from Seq0 import *

PORT = 8080
IP = "212.128.255.68"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

while True:
    print("Waiting for connection...")
    (client_socket, client_ip_port) = ls.accept()
    print("A client has connected to the server!")

    msg_raw = client_socket.recv(2048)
    message = msg_raw.decode()
    termcolor.cprint(f"Message received: {message}", "green")

    response = message
    answer = response.encode()
    client_socket.send(answer)
    client_socket.close()



ls.close()