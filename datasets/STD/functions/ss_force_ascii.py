from unidecode import unidecode

def force_ascii(input_seq):
    # Convert each string in the list to its ASCII representation
    output_seq = [unidecode(s) for s in input_seq]
    return output_seq

# Example usage
seq_a = [
    "Café",
    "naïve",
    "fiancé",
    "élève",
    "garçon"
]
seq_b = force_ascii(seq_a)
print(seq_b)