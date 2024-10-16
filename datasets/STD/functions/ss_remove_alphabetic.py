import re

def remove_alphabetic_letters(input_seq):
    # Remove all alphabetic letters for each string in the list
    output_seq = [re.sub(r'[a-zA-Z]', '', s) for s in input_seq]
    return output_seq

# Example usage
seq_a = ["Hello123", "Python $%^&*", "Programming 123"]
seq_b = remove_alphabetic_letters(seq_a)
print(seq_b)