import math

def apply_exp(input_seq):
    # Apply the exponential function to each number in the list
    output_seq = [math.exp(x) for x in input_seq]
    return output_seq

# Example usage
seq_a = [0, 1, 2, 3, 4, 5]
seq_b = apply_exp(seq_a)
print(seq_b)