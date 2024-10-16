import re

def extract_state(input_seq):
    # Define regex pattern to find state abbreviations or names
    state_pattern = r'\b(?:AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY)\b'
    
    output_seq = []
    for s in input_seq:
        # Find all occurrences of states in the string
        matches = re.findall(state_pattern, s)
        if matches:
            output_seq.append(matches[0])  # Append the first match found
        else:
            output_seq.append("")  # Append empty string if no match found
    
    return output_seq

# Example usage
seq_a = [
    "I live in California",
    "NYC is a great city",
    "TX is known for its BBQ",
    "She is from WA state",
    "No state mentioned here"
]
seq_b = extract_state(seq_a)
print(seq_b)