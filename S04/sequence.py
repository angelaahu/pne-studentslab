from pathlib import Path

FILENAME = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()
content = file_contents.split("\n")
sequence = "".join(content[1:])

print("The total number of bases:", len(sequence))