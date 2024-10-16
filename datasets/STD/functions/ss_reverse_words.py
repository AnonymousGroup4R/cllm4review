def reverse_words(input_seq):
    # Reverse each word in each string in the list
    output_seq = [' '.join(word[::-1] for word in s.split()) for s in input_seq]
    return output_seq

# Example usage
seq_a = ["hello world", "python programming", "open ai"]
seq_b = reverse_words(seq_a)
print(seq_b)