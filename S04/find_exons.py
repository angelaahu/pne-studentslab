from pathlib import Path

def clean_seq(lines):
    seq = []
    for line in lines:
        if not line.startswith(">"):
            seq.append(line.strip())
    return "".join(seq)


file1 = "sequences/ADA.txt"
file2 = "sequences/ADA_EXONS.txt"

file_contents = Path(file1).read_text()
exon_content = Path(file2).read_text()
gene_sequence = clean_seq(file_contents.splitlines())


exons = []
current = ""
for line in exon_content.splitlines():
    if line.startswith(">"):
        if current:
            exons.append(current)
            current = ""
    else:
        current += line.strip()

if current:
    exons.append(current)


max_coord = 44652852
print("Exon   | Length   | Start       |  End    ")
print("-" * 50)

exon_num = 1
for exon in exons:
    index = gene_sequence.find(exon)

    if index == -1:
        print("Exon", exon_num, "not found")
    else:
        length = len(exon)
        start = max_coord - index
        end = max_coord - (index + length - 1)

        if start > end:
            start, end = end, start

        print(f"{exon_num:<6} | {length:<8} | {start:<12} | {end:<14}")

    exon_num += 1