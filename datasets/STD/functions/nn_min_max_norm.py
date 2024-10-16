def min_max_normalize(input_seq):
    # Calculate the minimum and maximum values in the input sequence
    min_val = min(input_seq)
    max_val = max(input_seq)
    
    # Apply min-max normalization to each value in the input sequence
    output_seq = [(x - min_val) / (max_val - min_val) if max_val != min_val else 0 for x in input_seq]
    return output_seq

# Example usage
seq_a = [10, 20, 30, 40, 50]
seq_b = min_max_normalize(seq_a)
print(seq_b)