def convert_to_lowercase(input_seq):
    # Convert each string in the list to uppercase
    output_seq = [s.lower() for s in input_seq]
    return output_seq

# Example usage
seq_a = ["hello", "world", "Python", "programming"]
seq_b = convert_to_lowercase(seq_a)
print(seq_b)