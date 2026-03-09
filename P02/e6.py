from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.68"
PORT1 = 8080
PORT2 = 8081

c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
print(c1)
print(c2)

gene = "FRAT1"
s = Seq()
s.read_fasta("/home/alumnos/angelahu/PycharmProjects/pne-studentslab/S04/Sequences/" + gene + ".txt")

send_frat1 = c1.talk("Sending FRAT1 gene to the server, in fragments of 10 bases...")
send_frat2 = c2.talk("Sending FRAT1 gene to the server, in fragments of 10 bases...")
print(f"Gene FRAT1: {s}")

frag = ""
count = 0
i = 0
s_str = str(s)

while count < 10 and i < len(s_str):
    frag += s_str[i]
    i += 1
    if len(frag) == 10:
        count += 1
        message = f"Fragment {count}: {frag}"
        print(message)
        if count % 2 == 0:
            response = c2.talk(message)
        else:
            response = c1.talk(message)
        frag = ""

