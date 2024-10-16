import numpy as np

def z_score_normalization(input_seq):
    # Calculate mean and standard deviation of the input sequence
    mean = np.mean(input_seq)
    std_dev = np.std(input_seq)
    
    # Apply z-score normalization
    output_seq = [(x - mean) / std_dev for x in input_seq]
    return output_seq

# Example usage
seq_a = [10, 20, 30, 40, 50]
seq_b = z_score_normalization(seq_a)
print(seq_b)