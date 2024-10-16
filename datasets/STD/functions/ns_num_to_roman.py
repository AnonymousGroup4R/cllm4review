def int_to_roman(num):
    # Define the value mappings
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_numeral += syb[i]
            num -= val[i]
        i += 1
    return roman_numeral

def num_to_roman_list(num_list):
    return [int_to_roman(x) for x in num_list]

# Example test case
seq_a = [3, 4, 9, 58, 1994]
seq_b = num_to_roman_list(seq_a)
print(seq_b)