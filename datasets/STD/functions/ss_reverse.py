def reverse_items(str_list):
    # Apply the transformation to each string in the list
    res = [snake_str[::-1] for snake_str in str_list]
    return res

# Example usage
seq_a = ["this_is_an_example_string", "another_example_string", "yet_another_example"]
seq_b = reverse_items(seq_a)
print(seq_b)