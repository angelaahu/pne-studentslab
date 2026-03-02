from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")
# -- Create a Null sequence
s = Seq()
# -- Initialize the null seq with the given file in fasta format
s.read_fasta("/home/alumnos/angelahu/PycharmProjects/pne-studentslab/S04/sequences/U5.txt")


print(f"Sequence: (Length: {s.len()}) {s}")
print(f"  Bases: {s.count()}")
print(f"  Rev:   {s.reverse()}")
print(f"  Comp:  {s.complement()}")
