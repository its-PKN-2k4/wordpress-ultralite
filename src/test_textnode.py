import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq_string(self):
        node = TextNode("All the time you have to leave a space", TextType.ITALIC_TEXT)
        node2 = TextNode("All the time you have to leave space", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("Must be the water!", TextType.ITALIC_TEXT)
        node2 = TextNode("Must be the water!", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_not_eq_link(self):
        node = TextNode("We are checking...", "https://www.boot.dev")
        node2 = TextNode("We are checking...", "https://www.google.com")
        self.assertNotEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertNotEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()