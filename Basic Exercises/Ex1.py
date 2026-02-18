#Exercise 1: strings

dna = "ATGCGATCGATCGATCGATCGA"
print("The total length of the string is:", len(dna))
print("The first 5 characters:", dna[0:5])
print("The last 3 characters:", dna[-3::])
print("Lowercase:", dna.lower())
print("Count 'ATC':", dna.count("ATC"))
print("Replaced string:", dna.replace("T","U"))
