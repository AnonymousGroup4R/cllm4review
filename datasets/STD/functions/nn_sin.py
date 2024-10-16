import math

def apply_sin(input_seq):
    # Apply the sine function to each number in the list
    output_seq = [math.sin(x) for x in input_seq]
    return output_seq

# Example usage
seq_a = [0, math.pi/2, math.pi, 3*math.pi/2, 2*math.pi]
seq_b = apply_sin(seq_a)
print(seq_b)