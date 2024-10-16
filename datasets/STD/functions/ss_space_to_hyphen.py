def replace_spaces_with_hyphens(input_seq):
    # Replace spaces with hyphens for each string in the list
    output_seq = [s.replace(" ", "-") for s in input_seq]
    return output_seq

# Example usage
seq_a = ["hello world", "this is a test", "replace spaces with hyphens"]
seq_b = replace_spaces_with_hyphens(seq_a)
print(seq_b)