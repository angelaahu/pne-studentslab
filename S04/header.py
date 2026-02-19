from pathlib import Path

FILENAME = "sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()

content_new = file_contents.split("\n")
#print(content_new[0])

def get_header(seq):
    sequences = []
    space = " "
    for i in range(0,len(seq)):
        if (seq[i]).startswith(">") :
            sequences.append(seq[i])
    sequence = space.join(sequences)

    return (sequence.strip())

header = get_header(content_new)
print("First line of the", FILENAME,"file:")
print(header)

