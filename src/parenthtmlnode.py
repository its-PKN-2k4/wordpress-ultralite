from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError
        if self.children == None:
            raise ValueError("No children node founded")
        children_html = []
        for child in self.children:
            children_html.append(child.to_html())
        children_html = "".join(children_html)
        final = f'<{self.tag} {super().props_to_html()}>{children_html}</{self.tag}>' if self.props != None else f'<{self.tag}>{children_html}</{self.tag}>'
        return final