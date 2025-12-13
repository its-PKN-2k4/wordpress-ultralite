from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f'{self.value}'
        return f'<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>' if self.props != None else f'<{self.tag}>{self.value}</{self.tag}>'