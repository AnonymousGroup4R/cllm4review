import math

def apply_ceil_to_integers(input_seq):
    # Apply floor function to each element in the list
    output_seq = [math.ceil(x) for x in input_seq]
    return output_seq

# Example usage
seq_a = [1.1, 2.9, 3.5, 4.2, 5.7]
seq_b = apply_ceil_to_integers(seq_a)
print(seq_b)