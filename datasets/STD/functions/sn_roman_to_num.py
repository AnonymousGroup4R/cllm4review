def roman_to_int(s):
    # Dictionary to map Roman numerals to their integer values
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize total and previous value
    total = 0
    prev_value = 0
    
    # Loop through each character in the Roman numeral string
    for char in reversed(s):
        value = roman_dict[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

def transform_roman_list(str_list):
    return [roman_to_int(x) for x in str_list]

# Example usage
seq_a = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
seq_b = transform_roman_list(seq_a)
print(seq_b)