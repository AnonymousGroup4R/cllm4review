def format_emails_remove_dots(input_seq):
    # Remove dots in the username field for each email address in the list
    output_seq = []
    for email in input_seq:
        username, domain = email.split('@')
        username = username.replace('.', '')  # Remove dots from the username
        formatted_email = f"{username}@{domain}"
        output_seq.append(formatted_email)
    
    return output_seq

# Example usage
seq_a = ["user.name@example.com", "first.last@gmail.com", "john.doe@yahoo.com"]
seq_b = format_emails_remove_dots(seq_a)
print(seq_b)