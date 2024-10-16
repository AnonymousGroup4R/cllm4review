def bools_to_ints(input_s):
    # Convert each boolean in the list to an integer
    output_s = [int(b) for b in input_s]
    return output_s

# Example usage
seq_a = [True, False, True, True, False]
seq_b = bools_to_ints(seq_a)
print(seq_b)