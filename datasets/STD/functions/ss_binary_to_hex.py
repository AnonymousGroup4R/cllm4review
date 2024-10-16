def binary_to_hex(input_seq):
    # Convert binary strings to hexadecimal strings for each string in the list
    output_seq = []
    for binary_str in input_seq:
        # Ensure the binary string length is a multiple of 4 by padding if necessary
        padded_binary_str = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
        
        # Convert binary to hexadecimal
        hex_str = ''.join(hex(int(padded_binary_str[i:i+4], 2))[2:] for i in range(0, len(padded_binary_str), 4))
        
        output_seq.append(hex_str)
    
    return output_seq

# Example usage
seq_a = ["1010", "110101", "111000111"]
seq_b = binary_to_hex(seq_a)
print(seq_b)