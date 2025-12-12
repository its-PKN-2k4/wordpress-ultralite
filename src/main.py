from textnode import TextNode, TextType

def main():
    obj1 = TextNode("All the time you have to leave a space", TextType.LINK, "https://www.boot.dev")
    print(TextNode.__repr__(obj1))


if __name__ == "__main__":
    main()