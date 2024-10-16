def strings_to_bools(input_s):
    # Define mappings for truthy and falsy strings
    truthy_values = {"true", "1", "yes", "y", "on"}
    falsy_values = {"false", "0", "no", "n", "off"}
    
    # Convert each string in the list to a boolean
    output_s = []
    for s in input_s:
        lower_s = s.strip().lower()
        if lower_s in truthy_values:
            output_s.append(True)
        elif lower_s in falsy_values:
            output_s.append(False)
        else:
            raise ValueError(f"Invalid boolean string: {s}")
    
    return output_s

# Example usage
seq_a = ["true", "false", "1", "0", "yes", "no", "on", "off"]
seq_b = strings_to_bools(seq_a)
print(seq_b)