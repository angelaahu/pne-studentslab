from Seq0 import *

print("----- Exercise 8 ----")
genes = ["U5", "ADA", "FRAT1", "FXN"]

for gene in genes:
    files = "/home/alumnos/angelahu/PycharmProjects/pne-studentslab/S04/sequences/" + gene + ".txt"
    sequence = seq_read_fasta(files)
    bases_count = seq_count(sequence)

    most_repeated_base = ""
    highest_count = 0
    for base in bases_count:
        if bases_count[base] > highest_count:
            highest_count = bases_count[base]
            most_repeated_base = base

    print("Gene " + str(gene) + ": Most frequent Base:", most_repeated_base)

#alternative way using .items and dict
#for base, count in bases_count.items():
#   if count > highest_count:
#       highest_count = count
#       most_repeated_base = base

