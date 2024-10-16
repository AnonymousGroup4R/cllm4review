def check_space_in_string(input_seq):
    # Check if space is present in each string in the list
    output_seq = [' ' in s for s in input_seq]
    return output_seq

# Example usage
seq_a = ["hello world", "python", "programming language", "open ai"]
seq_b = check_space_in_string(seq_a)
print(seq_b)