from textnode import TextNode, TextType, text_node_to_html_node

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
