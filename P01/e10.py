from Seq1 import Seq

def most_frequent(bases_count):
    highest_count = 0
    most_repeated_base = ""
    for base in bases_count:
        if bases_count[base] > highest_count:
            highest_count = bases_count[base]
            most_repeated_base = base
    return most_repeated_base

print("-----| Practice 1, Exercise 10 |------")

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for gene in genes:
    file = "/home/alumnos/angelahu/PycharmProjects/pne-studentslab/S04/sequences/" + gene + ".txt"
    seq = Seq()
    seq.read_fasta(file)

    bases_count = seq.count()

    print("Gene " + str(gene) + ": Most frequent Base:", most_frequent(bases_count))