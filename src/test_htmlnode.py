import unittest

from htmlnode import HTMLNode

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