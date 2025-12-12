import unittest

from textnode import TextNode, TextType


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



if __name__ == "__main__":
    unittest.main()