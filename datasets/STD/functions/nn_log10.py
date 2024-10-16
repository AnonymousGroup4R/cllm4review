import math

def apply_log(input_seq):
    # Apply the sine function to each number in the list
    output_seq = [math.log10(x) for x in input_seq]
    return output_seq

# Example usage
seq_a = [1, math.e, 10, 100, 1000]
seq_b = apply_log(seq_a)
print(seq_b)