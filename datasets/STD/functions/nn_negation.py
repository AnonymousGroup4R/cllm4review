def compute_negations(input_seq):
    # Compute the negation for each number in the list
    output_seq = [-x for x in input_seq]
    return output_seq

# Example usage
seq_a = [0, 1, -2, 3, -4, 5]
seq_b = compute_negations(seq_a)
print(seq_b)