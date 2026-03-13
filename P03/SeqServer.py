import socket
from Seq1 import Seq
import termcolor

PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

while True:
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:

        print("A client has connected to the server!")

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        msg = str(msg.upper().strip())
        parts = msg.split()
        cmd = parts[0]

        if msg == "PING\n" or msg == "PING":
            termcolor.cprint(f"{msg} command!!", "yellow")
            print("OK\n")
            response = "OK!\n"
            cs.send(response.encode())
            cs.close()

        if msg[0:3] == "GET":

            genes = ["AAATTTCCCACGA", "AGGTATTCCACGA", "TTACAGTCAC", "GGCCTTAACGT", "AGGTAAGAT"]

            termcolor.cprint(f"GET", "yellow")
            parts = msg.split()
            index = int(parts[1])

            if 0 <= index < len(genes):
                print(genes[index] + "\n")
                response = genes[index] + "\n"
                cs.send(response.encode())

            else:
                cs.send(f"NOT A VALID INDEXs".encode())
                print("Not a valid index\n")
            cs.close()

        elif cmd == "INFO":
            sequence = parts[-1]
            termcolor.cprint(f"INFO", "yellow")
            seq = Seq(sequence)
            print(f"Sequence {seq}")
            count_dict = seq.count()
            tot = seq.len()
            print(f"Total length: {tot}")

            response = f"Sequence: {seq}\n"
            response += f"Total length: {tot}\n"
            for key, value in count_dict.items():
                percent = round((value / tot) * 100, 1)
                anws = f"{key}: {value} ({percent})%\n"
                print(anws.strip())
                response += anws
            cs.send(response.encode())
            cs.close()

        elif cmd == "COMP":
            sequence = parts[-1]
            termcolor.cprint(f"COMP", "yellow")
            seq = Seq(sequence)
            comp = seq.complement()
            print(f"Sequence {seq}")
            print(f"Complement: {comp}\n")
            response = comp
            cs.send(response.encode())
            cs.close()

        elif cmd == "REV":
            sequence = parts[-1]
            termcolor.cprint(f"REV", "yellow")
            seq = Seq(sequence)
            print(f"Sequence {seq}")
            rev = seq.reverse()
            print(f"Rwversed {rev}\n")
            response = seq.reverse()
            cs.send(response.encode())
            cs.close()

        elif cmd == "GENE":
            genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
            termcolor.cprint(f"GENE", "yellow")
            gene_name = parts[-1]

            if gene_name not in genes:
                print("Not valid gene name")
                cs.send(f"NOT A VALID GENE NAME".encode())

            else:
                file_name ="/Users/angel/Downloads/pne-studentslab-main (3)/pne-studentslab-main/S04/sequences/" + gene_name + ".txt"
                seq = Seq()
                seq.read_fasta(file_name)
                print(str(seq) + "\n")
                cs.send((str(seq) + "\n").encode())
                cs.close()

