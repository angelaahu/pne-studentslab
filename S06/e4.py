import termcolor
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


def generate_seqs(pattern, number):
    list = []
    for i in range(1, number + 1):
        list.append(Seq(pattern * i))
    return list


def print_seqs(seq_list, color):
    for i in range(len(seq_list)):
        termcolor.cprint(f"Sequence {i} : (Length: {seq_list[i].len()}) {seq_list[i]}", color)


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1, "blue")

print()
print("List 2:")
print_seqs(seq_list2, "green")