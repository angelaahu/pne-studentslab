from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.68"
PORT = 8080

c = Client(IP, PORT)
print(c)

genes = ["U5", "FRAT1", "ADA"]
for i in range(len(genes)):
    s = Seq()
    s.read_fasta(("/home/alumnos/angelahu/PycharmProjects/pne-studentslab/S04/Sequences/" + genes[i] + ".txt"))
    message = f"Sending the {genes[i]} Gene to the server..."
    print(f"To the Server: {message}")
    response = c.talk(message)
    print((f"To the Server: {response}"))
    print(f"To the Server: {s}")
    answer = c.talk(str(s))
    print(f"From Server:\n{answer}")


