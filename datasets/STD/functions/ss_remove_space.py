def remove_blanks(input_seq):
    # Remove blanks from each string in the list
    output_seq = [s.replace(" ", "").replace("\t", "").replace("\n", "") for s in input_seq]
    return output_seq

# Example usage
seq_a = [
    "Hello World",
    " This is a test\t",
    "\nNew Line\n",
    " Multiple   spaces "
]
seq_b = remove_blanks(seq_a)
print(seq_b)