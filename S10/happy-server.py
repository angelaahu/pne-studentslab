import socket

PORT = 8080
IP = "212.128.255.68"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for connection...")
    #Setting returning values
    (client_socket, client_ip_port) = ls.accept()
    print("A client has connected to the server!")

    msg_raw = client_socket.recv(2048)
    print("Received: ", msg_raw.decode())


    client_socket.send("Hello, I am the Happy server\n".encode())
    client_socket.close()


# -- Close the socket
ls.close()
