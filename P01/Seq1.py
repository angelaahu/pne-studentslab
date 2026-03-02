from pathlib import Path

class Seq:
    def __init__(self, strbases=None):
        self.strbases = strbases
        bases = ["A", "C", "G", "T"]
        valid = True

        if strbases is None:
            self.strbases = "NULL"
            print("NULL sequence created")

        else:
            for base in strbases:
                if base not in bases:
                    self.strbases = "ERROR"
                    valid = False

            if valid:
                print("New sequence created!")

            elif not valid:
                print("INVALID sequence created")


    def __str__(self):
        return self.strbases


    def len(self):
        if self.strbases == "NULL":
            result = 0
        elif self.strbases == "ERROR":
            result = 0
        elif self.strbases == self.strbases:
            result = len(self.strbases)
        return result


    def count_base(self, base):
        count = 0
        if self.strbases == "NULL":
            count = 0
        elif self.strbases == "ERROR":
            count = 0
        else:
            for i in self.strbases:
                if i == base:
                    count += 1
        return count


    def count(self):
        d = {"A": 0, "C": 0, "G": 0, "T": 0}

        if self.strbases == "NULL":
            return d
        elif self.strbases == "ERROR":
            return d

        else:
            for letter in self.strbases:
                if letter in d:
                    d[letter] += 1
            return d


    def reverse(self):
        if self.strbases == "NULL":
            rev = "NULL"
        elif self.strbases == "ERROR":
            rev = "ERROR"
        else:
            rev = self.strbases[::-1]
        return rev


    def complement(self):
        complement_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
        complement = ""
        if self.strbases == "NULL":
            complement = "NULL"
        elif self.strbases == "ERROR":
            complement = "ERROR"
        else:
            for base in self.strbases:
                complement += complement_dict[base]

        return complement


    def read_fasta(self, filename):
        file_content = Path(filename).read_text()
        code_lines = file_content.split("\n")
        sequences = []
        for line in code_lines:
            if line != "" and not line.startswith(">"):
                sequences.append(line.strip())
        self.strbases = "".join(sequences)
        return self.strbases


