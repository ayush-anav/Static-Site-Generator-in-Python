from split_delimiter import split_nodes_delimiter
import unittest
from textnode import TextNode, TextType

class TestDelimiter(unittest.TestCase):
    def test_delimiter(self):
        node = TextNode("Text with a code `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        test_case = [
            TextNode("Text with a code ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        
        self.assertEqual(new_nodes, test_case)