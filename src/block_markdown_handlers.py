from enum import Enum
import string

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks =  []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        cleaned_blocks.append(block)
    return cleaned_blocks

def block_to_block_type(markdown):
    markdown = markdown.strip()
    if check_heading_type(markdown):
        return BlockType.HEADING
    elif check_code_type(markdown):
        return BlockType.CODE
    elif check_quote_type(markdown):
        return BlockType.QUOTE
    elif check_unordered_list_type(markdown):
        return BlockType.UNORDERED_LIST
    elif check_ordered_list_type(markdown, 1):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def check_heading_type(block):
    if len(block) == 0:
        return False
    lines = block.splitlines()
    for line in lines:
        if not line.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### "), 0):
            return False
    return True

def check_code_type(block):
    if len(block) == 0:
        return False
    return block.startswith("```", 0) and block.endswith("```")

def check_quote_type(block):
    if len(block) == 0:
        return False
    lines = block.splitlines()
    for line in lines:
        if not line.startswith(">", 0):
            return False
    return True

def check_unordered_list_type(block):
    if len(block) == 0:
        return False
    lines = block.splitlines()
    for line in lines:
        if not line.startswith("- "):
            return False
    return True

def check_ordered_list_type(block, expected=1):
    if len(block) == 0:
        return False
    lines = block.splitlines()
    for line in lines:
        first_dot = line.find('.')
        if first_dot < 0:
            return False

        potential_num = line[:first_dot]
        if not potential_num.isdigit():
            return False

        n = int(potential_num)
        if n != expected:
            return False

        if len(line) <= (first_dot + 1) or line[first_dot + 1] != " ":
            return False
        expected = expected + 1
    return True   

def extract_title(markdown):
    if len(markdown) == 0:
        raise Exception("Invalid markdown: empty content")
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            title = line.split(" ", 1)[1]
            return title.strip()
    raise Exception("No top-level heading found in parsed markdown")