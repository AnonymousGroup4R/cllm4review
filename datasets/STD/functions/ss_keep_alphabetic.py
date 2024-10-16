import re

def keep_alphabetic_and_spaces(input_seq):
    # Keep only alphabetic letters and spaces for each string in the list
    output_seq = [re.sub(r'[^a-zA-Z\s]', '', s) for s in input_seq]
    return output_seq

# Example usage
seq_a = ["Hello123", "Python $%^&*", "Programming 123"]
seq_b = keep_alphabetic_and_spaces(seq_a)
print(seq_b)