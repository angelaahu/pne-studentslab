from Seq1 import Seq

def most_repeated():

    most_repeated_base = ""
    highest_count = 0
    for base in bases_count:
        if bases_count[base] > highest_count:
            highest_count = bases_count[base]
            most_repeated_base = base


print("-----| Practice 1, Exercise 10 |------")

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for gene in genes:
    file = "/home/alumnos/angelahu/PycharmProjects/pne-studentslab/S04/sequences/" + gene + ".txt"
    seq = Seq()
    seq.read_fasta(file)

    sequence = seq.read_fasta(files)
    bases_count = seq.count()

    most_repeated_base = ""
    highest_count = 0
    for base in bases_count:
        if bases_count[base] > highest_count:
            highest_count = bases_count[base]
            most_repeated_base = base

    print("Gene " + str(gene) + ": Most frequent Base:", most_repeated_base)