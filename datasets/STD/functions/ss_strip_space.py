def strip_whitespace(input_seq):
    # Strip leading and trailing whitespace for each string in the list
    output_seq = [s.strip() for s in input_seq]
    return output_seq

# Example usage
seq_a = ["  hello , world  ", "  Python  ", "  programming  "]
seq_b = strip_whitespace(seq_a)
print(seq_b)