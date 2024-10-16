def transform_to_abs(input_seq):
    # Convert each numerical value in the list to its absolute value
    output_seq = [abs(x) for x in input_seq]
    return output_seq

# Example usage
seq_a = [-10, 5, -3.5, 2, -100, 0]
seq_b = transform_to_abs(seq_a)
print(seq_b)