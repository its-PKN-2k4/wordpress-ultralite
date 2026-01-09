from textnode import TextNode, TextType
from copy_dir_to_dir import copy_dir_to_dir
from page_generator import generate_page

def main():
    #obj1 = TextNode("All the time you have to leave a space", TextType.LINK, "https://www.boot.dev")
    #print(TextNode.__repr__(obj1))
    copy_dir_to_dir("./static", "./public")
    generate_page("./content/index.md", "./template.html", "./public/index.html")


if __name__ == "__main__":
    main()