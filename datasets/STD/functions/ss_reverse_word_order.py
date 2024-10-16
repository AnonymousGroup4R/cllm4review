def reverse_word_order(input_seq):
    # Reverse the order of words in each string in the list
    output_seq = [' '.join(s.split()[::-1]) for s in input_seq]
    return output_seq

# Example usage
seq_a = ["Hello world", "Python is awesome", "OpenAI is doing great", "This is a sentence"]
seq_b = reverse_word_order(seq_a)
print(seq_b)