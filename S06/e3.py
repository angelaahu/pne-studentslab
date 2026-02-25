class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        self.strbases = strbases
        bases = ["A", "C", "G", "T"]

        valid = True
        for base in strbases:
            if base not in bases:
                valid = False

        if valid:
            self.strbases = strbases
            print("New sequence created!")

        else:
            self.strbases = "ERROR"
            print("Error, incorrect sequence!")


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

def print_seqs(seq_list):
    for i in range(len(seq_list)):
        print("Sequence", i, f": (Length: {seq_list[i].len()})", seq_list[i])


def generate_seqs(patter, number):








seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
