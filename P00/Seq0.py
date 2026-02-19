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
