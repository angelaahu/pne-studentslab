from Seq0 import *

file = "/home/alumnos/angelahu/PycharmProjects/pne-studentslab/S04/sequences/U5.txt"
gene_U5 = seq_read_fasta(file)
fragment = gene_U5[:20]

print("------ Exercise 6 ------")
print("Gene U5")
print("Original:", fragment)
print("Reversed:", seq_reverse(fragment, 20))

