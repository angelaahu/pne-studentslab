from Seq0 import *
l_bases = ["A", "C", "G", "T"]
genes = ["U5", "ADA", "FRAT1", "FXN"]

for i in range(0, len(genes)):
    files = "/home/alumnos/angelahu/PycharmProjects/pne-studentslab/S04/sequences/" + genes[i] + ".txt"
    sequence = seq_read_fasta(files)
    print("\nGene " + genes[i] + ":")
    for base in l_bases:
        count = seq_count_base(sequence, base)
        print(str(base) + ": " + str(count))
        