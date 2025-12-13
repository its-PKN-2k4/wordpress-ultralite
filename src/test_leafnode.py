import unittest

from htmlnode import HTMLNode
from leafhtmlnode import LeafNode

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