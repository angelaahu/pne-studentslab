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
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
