def convert_to_uppercase(input_seq):
    # Convert each string in the list to uppercase
    output_seq = [s.upper() for s in input_seq]
    return output_seq

# Example usage
seq_a = ["hello", "world", "Python", "programming"]
seq_b = convert_to_uppercase(seq_a)
print(seq_b)