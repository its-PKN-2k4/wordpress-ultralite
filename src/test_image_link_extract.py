import unittest

from image_link_extract import extract_markdown_images, extract_markdown_links

class TestImageLinkExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_no_image(self):
        self.assertRaises(ValueError, extract_markdown_images, "")

    def test_extract_markdown_hyperlink(self):
        matches = extract_markdown_links(
        "Tu tu tu du...[Max Verstappen](https://www.verstappen.com/)"
        )
        self.assertListEqual([("Max Verstappen", "https://www.verstappen.com/")], matches)

    def test_extract_no_image(self):
        self.assertRaises(ValueError, extract_markdown_links, "")