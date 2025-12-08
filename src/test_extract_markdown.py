import unittest
from extract_markdown_methods import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestMDExtraction(unittest.TestCase):
    def test_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_links(self):
        matches = extract_markdown_links(
            "This is the best website to learn non-glaze pls, [bootdev](https://boot.dev)"
        )
        self.assertEqual([("bootdev", "https://boot.dev")], matches)
        
    def test_split_images(self):

        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ], new_nodes
        )
        
    def test_split_link(self):
        node = TextNode("The best [website](https://boot.dev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        
        self.assertEqual(
            [
                TextNode("The best ", TextType.TEXT),
                TextNode("website", TextType.LINK, "https://boot.dev")
            ], new_nodes
        )