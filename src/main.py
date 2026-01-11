from textnode import TextNode, TextType
from copy_dir_to_dir import copy_dir_to_dir
from page_generator import generate_page_recursive
import sys

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    media_trove = "./static"
    content_trove = "./content"
    deployment_dir = "./docs"
    htmlframe_loc = "./template.html"

    print("Copying resources from 'static' to 'docs' for deployment...")
    copy_dir_to_dir(media_trove, deployment_dir)

    print("Building pages from markdown contents and HTML frame then push to deployment directory...")
    generate_page_recursive(content_trove, htmlframe_loc, deployment_dir, basepath)


if __name__ == "__main__":
    main()