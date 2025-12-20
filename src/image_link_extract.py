import re 

def extract_markdown_images(text):
    if len(text) <= 0:
        raise ValueError("Invalid image syntax in markdown: no url and/or no alt text")
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    if len(text) <= 0:
        raise ValueError("Invalid text linking syntax in markdown: no url and/or no linking text")
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)