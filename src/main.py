from textnode import TextNode, TextType
from copy_dir_to_dir import copy_dir_to_dir
from page_generator import generate_page_recursive

def main():
    #obj1 = TextNode("All the time you have to leave a space", TextType.LINK, "https://www.boot.dev")
    #print(TextNode.__repr__(obj1))
    copy_dir_to_dir("./static", "./public")
    copy_dir_to_dir("./static/images", "./public/images")
    generate_page_recursive("./content", "./template.html", "./public")


if __name__ == "__main__":
    main()