from pathlib import Path
#e1
def seq_ping():
    print("Ok")
#e2
def seq_read_fasta(filename):
    file_content = Path(filename).read_text()
    code_lines = file_content.split("\n")
    sequences = []
    for line in code_lines:
        if line != "" and not line.startswith(">"):
            sequences.append(line.strip())
    sequence = "".join(sequences)
    return sequence
#e3
def seq_len(seq):
    return len(seq)
#e4
def seq_count_base(seq, base):
    #return seq.count(base)
    count = 0
    for letter in seq:
        if letter == base:
            count += 1
    return count
#e5
def seq_count(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for letter in seq:
        if letter in d:
            d[letter] += 1
    return d
#e6
def seq_reverse(seq, n):
    list = []
    seq_rev = seq[::-1]
    for letter in seq_rev:
        if len(list) < n:
            list.append(letter)
    new_seq = "".join(list)
    return new_seq
#e7
def seq_complement(seq):
    complement_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
    complement = ""
    for base in seq:
        complement += complement_dict[base]
    return complement



