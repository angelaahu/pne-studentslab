import socket
import termcolor
from pathlib import Path

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # -- Generate the response message
    # It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    # -- Let's start with the body
    # This new contents are written in HTML language

    parts = req_line.split(" ")
    path = parts[1]
    # -- Constant with the new of the file to open

    FILENAME_A = "html/info/A.html"
    FILENAME_C = "html/info/C.html"
    INDEX = "html/info/index.html"
    G_FILE = "html/info/G.html"
    T_FILE = "html/info/T.html"
    ERROR_FILE = "html/info/error.html"


    if path == "/info/A":
        body = Path(FILENAME_A).read_text()
    elif path == "/info/C":
        body = Path(FILENAME_C).read_text()
    elif path == "/info/G":
        body = Path(G_FILE).read_text()
    elif path == "/info/T":
        body = Path(T_FILE).read_text()
    elif path == "/":
        body = Path(INDEX).read_text()
    else:
        body = Path(ERROR_FILE).read_text()



    # body = Path(FILENAME_A).read_text()

    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("Echo server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()
