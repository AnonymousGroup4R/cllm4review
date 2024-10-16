import re

def remove_content_in_brackets(input_seq):
    # Remove all content within brackets for each string in the list
    output_seq = [re.sub(r'\[[^\]]*\]|\([^)]*\)|\{[^}]*\}', '', s) for s in input_seq]
    return output_seq

# Example usage
seq_a = ["Hello [World]", "Python (Programming)", "Open {AI} (Artificial Intelligence)"]
seq_b = remove_content_in_brackets(seq_a)
print(seq_b)