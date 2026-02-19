from Seq0 import *

file = "/home/alumnos/angelahu/PycharmProjects/pne-studentslab/S04/sequences/U5.txt"
gene_U5 = seq_read_fasta(file)
fragment = gene_U5[:20]

print("------ Exercise 7 ------")
print("Gene U5")
print("Original frag:", fragment)
print("Complementary:", seq_complement(fragment))

