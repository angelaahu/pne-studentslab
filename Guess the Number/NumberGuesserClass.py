import socket
import random

class NumberGuesser:
    def __init__(self, secret_number = None, attempts = None):
        self.secret_number = secret_number
        self.attempts = attempts

    def guess(self, number):
        #result = 0
        #if number != self.secret_number:
         #   count += 1
        if number == self.secret_number:
            result = f"You won after {len(self.attempts)} attempts"
        elif number > self.secret_number:
            result = "Lower"
        elif number < self.secret_number:
            result = "Higher"
        return result

    def __str__(self):
        return self.secret_number, self.attempts


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP = "127.0.0.1"
PORT = 8081

ls.bind((IP, PORT))
ls.listen()

n = random.randint(1, 100)
attempts_list = []

while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Game stopped by the user")
        ls.close()
        exit()

    else:
        print("A client has connected to the game!!")
        print(n)
        game= NumberGuesser(n, attempts_list)
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        att_n = int(msg)
        attempt, attempts_list  = game.guess(att_n)
        if len(attempts_list) <= 20:
            send = attempt + "\n" + f"Numbers tried: {attempts_list}"
            cs.send(send.encode())
            if attempt != "lower" and attempt != "Higher":
                cs.close()

        else:
            response = "You are too bad for the game"
            cs.send(response.encode())
            cs.close()
        