def ascii_to_next_ascii(input_seq):
    # Convert each ASCII value to the next ASCII value for each string in the list
    output_seq = []
    for s in input_seq:
        converted_string = ''.join(chr(ord(char) + 1) for char in s)
        output_seq.append(converted_string)
    
    return output_seq

# Example usage
seq_a = ["Hello", "Python", "ASCII"]
seq_b = ascii_to_next_ascii(seq_a)
print(seq_b)