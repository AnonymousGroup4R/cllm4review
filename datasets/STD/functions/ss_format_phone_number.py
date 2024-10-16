def format_phone_numbers(input_seq):
    # Format phone numbers for each string in the list
    output_seq = []
    for s in input_seq:
        # Remove all non-digit characters
        cleaned_number = ''.join(filter(str.isdigit, s))
        
        # Format as (xxx) xxx-xxxx
        formatted_number = f"({cleaned_number[0:3]}) {cleaned_number[3:6]}-{cleaned_number[6:]}"

        output_seq.append(formatted_number)
    
    return output_seq

# Example usage
seq_a = ["(123) 456-7890", "1234567890", "123.456.7890", "123-4567890"]
seq_b = format_phone_numbers(seq_a)
print(seq_b)