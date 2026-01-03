import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_empty_props(self):
        node = HTMLNode("h1", "Hello World", None, None)
        node2 = HTMLNode("h2", "Goodbye World", None, None)
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_different_props_string(self):
        node = HTMLNode("p", "Karma!", None, {"style":"red"})
        node2 = HTMLNode("p", "Karma!", None, None)
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_same_props_string(self):
        node = HTMLNode("blockquote", "Simply lovely", None, {"style":"blue"})
        node2 = HTMLNode("p", "I know what to do!", None, {"style":"blue"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

class TestTextNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "The pinnacle of motorsport", {"href":"https://www.formula1.com/"})
        self.assertEqual(node.to_html(), '<a href="https://www.formula1.com/">The pinnacle of motorsport</a>')

    def test_leaf_to_html_img(self):
        node = LeafNode("img", "Trust me bro", {"src":"here.jpeg", "width":"800", "height":"800"})
        self.assertEqual(node.to_html(), '<img src="here.jpeg" width="800" height="800">Trust me bro</img>')

class TestHTMLNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_greatgrandchildren(self):
        great_grandchild_node = LeafNode("b", "grandchild")
        grandchild_node = ParentNode("h4", [great_grandchild_node], {"style": "red"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><h4 style="red"><b>grandchild</b></h4></span></div>',
        )


if __name__ == "__main__":
    unittest.main()