import re

def camel_to_snake_list(camel_str_list):
    def camel_to_snake(camel_str):
        # Replace capital letters with an underscore followed by the lowercase letter
        snake_str = re.sub('([A-Z])', r'_\1', camel_str).lower()
        return snake_str
    
    # Apply the transformation to each string in the list
    res = [camel_to_snake(camel_str) for camel_str in camel_str_list]
    return res

# Example usage
seq_a = ["thisIsAnExampleString", "anotherExampleString", "yetAnotherExample"]
seq_b = camel_to_snake_list(seq_a)
print(seq_b)