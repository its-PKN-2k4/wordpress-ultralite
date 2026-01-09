import unittest

from block_markdown_handlers import *

class TestMarkdownToBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestMarkdownBlockClassification(unittest.TestCase):
    def test_markdown_heading_type(self):
        md = """
# Never gonna give you up
## Never gonna let you down 
### Never gonna run around and desert you
#### Never gonna make you cry
##### Never gonna say goodbye
        """
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_markdown_code_type(self):
        md = """
``` 
s = "The future is now, old man"
print(len(s))  
```
        """
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_markdown_quote_type(self):
        md = """
> Never gonna give you up
> Never gonna let you down 
> Never gonna run around and desert you
> Never gonna make you cry
> Never gonna say goodbye
        """
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_markdown_unordered_type(self):
        md = """
- Never gonna give you up
- Never gonna let you down 
- Never gonna run around and desert you
- Never gonna make you cry
- Never gonna say goodbye
        """
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

    def test_markdown_ordered_type(self):
        md = """
1. Never gonna give you up
2. Never gonna let you down 
3. Never gonna run around and desert you
4. Never gonna make you cry
5. Never gonna say goodbye
        """
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)

    def test_extract_title(self):
        md = """
# The Greatest Technicians That's Ever Lived

1. Andy
2. Lupe
3. Zac
        """
        self.assertEqual(extract_title(md), "The Greatest Technicians That's Ever Lived")

    def test_extract_title_failure(self):
        md = """
## Companies that betrays GAMERS:

1. NVIDIA
2. AMD
3. Micron
        """
        self.assertRaises(Exception, extract_title, md)

if __name__ == "__main__":
    unittest.main()