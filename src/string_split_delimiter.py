from textnode import TextNode, TextType, text_node_to_html_node
import image_link_extract

def split_nodes_at_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
            continue
        node_splits = []
        sections = old.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown syntax, closing symbol for markdown section not found")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                node_splits.append(TextNode(sections[i], TextType.TEXT))
            else:
                node_splits.append(TextNode(sections[i], text_type))
        new_nodes.extend(node_splits)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
            continue

        remaining = old.text
        images = image_link_extract.extract_markdown_images(remaining)

        if len(images) == 0:
            continue
        for (image_alt, image_link) in images:
            sections = remaining.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0]))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            remaining = sections[1]
        
        if remaining != "":
            new_nodes.append(TextNode(remaining))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
            continue

        remaining = old.text
        links = image_link_extract.extract_markdown_links(remaining)

        if len(links) == 0:
            continue
        for (link_text, hyperlink) in links:
            sections = remaining.split(f"[{link_text}]({hyperlink})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0]))
            new_nodes.append(TextNode(link_text, TextType.LINK, hyperlink))
            remaining = sections[1]
        
        if remaining != "":
            new_nodes.append(TextNode(remaining))
    return new_nodes
