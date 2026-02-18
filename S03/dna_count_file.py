f = open("dna.txt" , "r")

lines = f.readlines()
f.close()

total = 0
a = 0
c = 0
g= 0
t = 0

for sequence in lines:
    sequence = sequence.strip()
    total += len(sequence)

    for base in sequence:
        if base == "A":
            a += 1
        elif base == "C":
            c += 1
        elif base == "G":
            g += 1
        elif base == "T":
            t += 1

print("Total number of bases:",total)
print("Number of A:", a)
print("Number of C:", c)
print("Number of G:", g)
print("Numebr of T:", t)



#from dna_count import count_bases
#if __name__ == "__main__":
    # main()

