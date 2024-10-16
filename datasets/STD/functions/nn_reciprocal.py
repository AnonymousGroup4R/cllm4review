def compute_reciprocal(input_seq):
    # Compute reciprocal (1/value) for each element in the list
    output_seq = [1 / x for x in input_seq]
    return output_seq

# Example usage
seq_a = [1, 2, 3, 4, 5]
seq_b = compute_reciprocal(seq_a)
print(seq_b)