from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

seq_l = [s1, s2, s3]

bases = ["A", "C", "G", "T"]

for seq in seq_l:
    index = seq_l.index(seq)
    print(f"Sequence {index}: (Length: {seq.len()}) {seq}")

    for base in bases:
        print(f"{base}: {seq.count_base(base)} ")
