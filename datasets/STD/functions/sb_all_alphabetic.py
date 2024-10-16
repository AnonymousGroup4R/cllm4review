def check_all_alphabetic(input_seq):
    # Check if each string in the list is alphabetic
    output_seq = [s.isalpha() for s in input_seq]
    return output_seq

# Example usage
seq_a = ["Hello", "Python", "123", "Programming"]
seq_b = check_all_alphabetic(seq_a)
print(seq_b)