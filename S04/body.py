from pathlib import Path

FILENAME = "sequences/U5.txt"
file_contents = Path(FILENAME).read_text()

content_new = file_contents.split("\n")

print("Body of the", FILENAME,"file:")
print("".join(content_new[1:]))