def remove_all_brackets(input_seq):
    # Remove all types of brackets from each string in the list
    brackets = ['(', ')', '[', ']', '{', '}']
    output_seq = [s.translate(str.maketrans('', '', ''.join(brackets))) for s in input_seq]
    return output_seq

# Example usage
seq_a = ["(Hello) [world]", "{Python} [programming]"]
seq_b = remove_all_brackets(seq_a)
print(seq_b)