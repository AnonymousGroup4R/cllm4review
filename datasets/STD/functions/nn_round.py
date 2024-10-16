def round_to_integers(input_seq):
    # Round each element in the list to the nearest integer
    output_seq = [round(x) for x in input_seq]
    return output_seq

# Example usage
seq_a = [1.1, 2.9, 3.5, 4.2, 5.7]
seq_b = round_to_integers(seq_a)
print(seq_b)