from markdown_to_html import *
from block_markdown_handlers import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}...')
    with open(from_path, 'r') as mdfile:
        md = mdfile.read()

    with open(template_path, 'r') as htmlframe:
        template = htmlframe.read()

    parent_html = markdown_to_html_node(md).to_html()
    page_tile = extract_title(md)

    template = template.replace("{{ Title }}", page_tile)
    template = template.replace("{{ Content }}", parent_html)

    directory = os.path.dirname(dest_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(dest_path, 'w') as newfile:
        newfile.write(template)