from Seq0 import *

genes = ["U5", "ADA", "FRAT1", "FXN"]

for gene in genes:
    files = "/home/alumnos/angelahu/PycharmProjects/pne-studentslab/S04/sequences/" + gene + ".txt"
    sequence = seq_read_fasta(files)
    #bases_count = seq_count(sequence)
    print("Gene " + str(gene) + ": ", seq_count(sequence))
