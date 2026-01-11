from markdown_to_html import *
from block_markdown_handlers import extract_title
import os
from pathlib import Path

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

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)

    for fname in files:
        src_path = Path(os.path.join(dir_path_content, fname))
        if src_path.suffix.lower() == '.md':
            dest_file_path = Path(os.path.join(dest_dir_path, fname)).with_suffix('.html')
            generate_page(os.path.join(dir_path_content, fname), template_path, dest_file_path)
        elif src_path.is_dir():
            generate_page_recursive(src_path, template_path, Path(os.path.join(dest_dir_path, fname)))
        else:
            continue
