def title_elements(input_seq):
    # Capitalize the first letter of each string in the list
    output_seq = [s.title() for s in input_seq]
    return output_seq

# Example usage
seq_a = ["hello world", "python programming"]
seq_b = title_elements(seq_a)
print(seq_b)