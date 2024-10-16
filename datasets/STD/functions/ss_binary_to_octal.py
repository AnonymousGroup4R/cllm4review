def binary_to_octal(input_seq):
    # Convert binary strings to octal strings for each string in the list
    output_seq = []
    for binary_str in input_seq:
        # Ensure the binary string length is a multiple of 3 by padding if necessary
        padded_binary_str = binary_str.zfill((len(binary_str) + 2) // 3 * 3)
        
        # Convert binary to octal
        octal_str = ''.join(str(int(padded_binary_str[i:i+3], 2)) for i in range(0, len(padded_binary_str), 3))
        
        output_seq.append(octal_str)
    
    return output_seq

# Example usage
seq_a = ["1010", "110101", "111000111"]
seq_b = binary_to_octal(seq_a)
print(seq_b)