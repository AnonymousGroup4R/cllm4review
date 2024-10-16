import markdown

def markdown_to_html(input_seq):
    # Convert each Markdown string in the list to HTML
    output_seq = [markdown.markdown(md) for md in input_seq]
    return output_seq

# Example usage
seq_a = [
    "# Heading 1",
    "## Heading 2",
    "**Bold text**",
    "*Italic text*",
    "[Link](https://www.example.com)",
    "- List item"
]
seq_b = markdown_to_html(seq_a)
print(seq_b)