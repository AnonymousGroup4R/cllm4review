def replace_spaces_with_underscores(input_seq):
    # Replace spaces with underscores for each string in the list
    output_seq = [s.replace(" ", "_") for s in input_seq]
    return output_seq

# Example usage
seq_a = ["hello world", "this is a test", "replace spaces with underscores"]
seq_b = replace_spaces_with_underscores(seq_a)
print(seq_b)