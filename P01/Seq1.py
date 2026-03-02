class Seq:

    def __init__(self, strbases=None):

        self.strbases = strbases
        bases = ["A", "C", "G", "T"]

        if strbases == None:
            self.strbases = "NULL"
            print("NULL sequence created")

        else:
            for base in strbases:
                if base not in bases:
                    self.strbases = "ERROR"
                    print("Invalid sequence created")
                    return

            self.strbases = strbases
            print("New sequence created")



    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)



