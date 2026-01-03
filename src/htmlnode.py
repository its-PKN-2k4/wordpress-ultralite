class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None or len(self.props) <= 0:
            return ""
        props_list = []
        for attr in self.props:
            val = self.props[attr]
            full_attr = f'{attr}="{val}"'
            props_list.append(full_attr)

        return " ".join(props_list)

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f'{self.value}'
        return f'<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>' if self.props != None else f'<{self.tag}>{self.value}</{self.tag}>'

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