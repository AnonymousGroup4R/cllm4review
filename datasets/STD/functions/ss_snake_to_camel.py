def snake_to_camel_list(snake_str_list):
    def snake_to_camel(snake_str):
        # Split the snake_case string into parts
        components = snake_str.split('_')
        # Capitalize the first letter of each part except the first one and join them
        camel_str = components[0] + ''.join(x.capitalize() for x in components[1:])
        return camel_str
    
    # Apply the transformation to each string in the list
    res = [snake_to_camel(snake_str) for snake_str in snake_str_list]
    return res

# Example usage
seq_a = ["this_is_an_example_string", "another_example_string", "yet_another_example"]
seq_b = snake_to_camel_list(seq_a)
print(seq_b)