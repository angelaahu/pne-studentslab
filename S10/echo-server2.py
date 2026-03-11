import socket
import termcolor
PORT = 8080
IP = "212.128.255.68"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

connection = 0

print("The server is configured!")

while True:
    print("Waiting for connection...")
    try:
        (client_socket, client_ip_port) = ls.accept()
        connection += 1

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        print("A client has connected to the server!")
        msg_raw = client_socket.recv(2048)
        message = msg_raw.decode()
        termcolor.cprint(f"Message received: {message}", "green")

        print("Connection: ", connection, "Client (IP, PORT): ", client_ip_port)

        response = "ECHO: " + message
        client_socket.send(response.encode())
        client_socket.close()


