import math

def apply_tan(input_seq):
    # Apply the sine function to each number in the list
    output_seq = [x * 10 for x in input_seq]
    return output_seq

# Example usage
seq_a = [0, 1, 2, 3, 10, 90]
seq_b = apply_tan(seq_a)
print(seq_b)