from pathlib import Path

def seq_ping():
    print("Ok")

def seq_read_fasta(filename):
    file_content = Path(filename).read_text()
    code_lines = file_content.split("\n")
    sequences = []
    for line in code_lines:
        if line != "" and not line.startswith(">"):
            sequences.append(line.strip())
    sequence = "".join(sequences)
    return sequence

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    #return seq.count(base)
    count = 0
    for letter in seq:
        if letter == base:
            count += 1
    return count

def seq_count(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for letter in seq:
        if letter in d:
            d[letter] += 1
    return d

def seq_reverse(seq, n):
    list = []
    seq_rev = seq[::-1]
    for letter in seq_rev:
        if len(list) < n:
            list.append(letter)
    new_seq = "".join(list)
    return new_seq



