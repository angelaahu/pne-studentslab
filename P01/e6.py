from Seq1 import Seq

print("-----| Practice 1, Exercise 6 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

seq_l = [s1, s2, s3]

for i in seq_l:
    index = seq_l.index(i)
    length = i.len()
    print(f"Sequence {index}: (Length: {length}) {i}")

    print(f"Bases: {i.count()}")