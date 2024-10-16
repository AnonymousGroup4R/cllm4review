def add_previous_to_current(input_seq):
    # Initialize an empty list for the output sequence
    output_seq = []
    
    # Iterate through the input sequence
    for i in range(len(input_seq)):
        # Add the current element to the previous element (if exists)
        if i == 0:
            output_seq.append(input_seq[i])
        else:
            output_seq.append(input_seq[i] + input_seq[i-1])
    
    return output_seq

# Example usage
seq_a = [1, 2, 3, 4, 5]
seq_b = add_previous_to_current(seq_a)
print(seq_b)