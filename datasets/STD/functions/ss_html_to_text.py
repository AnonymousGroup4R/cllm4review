from bs4 import BeautifulSoup

def html_to_text(input_seq):
    # Convert each HTML string in the list to plain text
    output_seq = [BeautifulSoup(html, "html.parser").get_text() for html in input_seq]
    return output_seq

# Example usage
seq_a = [
    "<p>This is a <b>bold</b> paragraph.</p>",
    "<div>Hello, <i>world</i>!</div>",
    "<h1>Heading</h1><p>Some text here.</p>"
]
seq_b = html_to_text(seq_a)
print(seq_b)