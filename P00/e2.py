from Seq0 import seq_read_fasta
seq = seq_read_fasta("/home/alumnos/angelahu/PycharmProjects/pne-studentslab/S04/sequences/U5.txt")

list = []
for base in seq:
    if len(list) < 20:
        list.append(base)

first20 = list[:20]
print("DNA file: U5.txt")
print("The first 20 bases are:")
print("".join(first20))