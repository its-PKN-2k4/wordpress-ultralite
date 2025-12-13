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
            full_attr = f'{attr}={val}'
            props_list.append(full_attr)

        return " ".join(props_list)

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'