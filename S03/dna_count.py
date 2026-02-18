def count_bases(seq):
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for base in seq:
        if base == "A":
            count_a += 1
        elif base == "C":
            count_c += 1
        elif base == "G":
            count_g += 1
        elif base == "T":
            count_t += 1

    return count_a, count_c, count_g, count_t

sequence = (input("Enter the DNA sequence: ")).upper()
a, c, g, t = count_bases(sequence)
print("Total length of the sequence: ", len(sequence))
print("A:", a)
print("C:", c)
print("G:", g)
print("T:", t)
