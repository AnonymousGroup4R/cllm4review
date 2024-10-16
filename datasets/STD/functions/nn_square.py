def compute_square(input_seq):
    # Compute square for each element in the list
    output_seq = [x ** 2 for x in input_seq]
    return output_seq

# Example usage
seq_a = [1, 2, 3, 4, 5]
seq_b = compute_square(seq_a)
print(seq_b)