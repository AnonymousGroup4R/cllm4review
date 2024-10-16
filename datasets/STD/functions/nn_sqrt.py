import math

def compute_square_roots(input_seq):
    # Compute the square root for each number in the list
    output_seq = [math.sqrt(x) for x in input_seq]
    return output_seq

# Example usage
seq_a = [0, 1, 4, 9, 16, 25]
seq_b = compute_square_roots(seq_a)
print(seq_b)