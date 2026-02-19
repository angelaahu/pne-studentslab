from Seq0 import *

genes = ["U5", "ADA", "FRAT1", "FXN"]

for i in range(0, len(genes)):
    sequence = seq_read_fasta("/home/alumnos/angelahu/PycharmProjects/pne-studentslab/S04/sequences/" + genes[i] + ".txt")
    print("Gene", genes[i], "->", seq_len(sequence))