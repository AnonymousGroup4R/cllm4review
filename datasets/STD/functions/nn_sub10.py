import math

def apply_sub10(input_seq):
    # Apply the sine function to each number in the list
    output_seq = [x - 10 for x in input_seq]
    return output_seq

# Example usage
seq_a = [0, 10, 100, 20]
seq_b = apply_sub10(seq_a)
print(seq_b)