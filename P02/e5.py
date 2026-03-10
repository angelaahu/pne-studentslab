from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.68"
PORT = 8080

c = Client(IP, PORT)
print(c)

gene = "FRAT1"
s = Seq()
s.read_fasta("/home/alumnos/angelahu/PycharmProjects/pne-studentslab/S04/sequences/" + gene + ".txt")

send_frat = c.talk("Sending FRAT1 gene to the server, in fragments of 10 bases...")
print(f"Gene FRAT1: {s}")

frag = ""
count = 0
i = 0
s_str = str(s)

while count < 5 and i < len(s_str):
    frag += s_str[i]
    i += 1
    if len(frag) == 10:
        count += 1
        message = f"Fragment {count}: {frag}"
        print(message)
        m_frag = c.talk(message)
        frag = ""