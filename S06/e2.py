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

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)
