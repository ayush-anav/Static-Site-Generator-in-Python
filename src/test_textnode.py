import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
        
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("Another node", TextType.ITALIC)
        node4 = TextNode("This is an image", TextType.IMAGE, url="blahblah")
        node5 = TextNode("This is another image, but broken", TextType.IMAGE)
        
        # if inputs equal, passes
        self.assertEqual(node, node2)
        
        # if inputs not equal, fails
        self.assertNotEqual(node3, node4)
        
        # This test will fail
        # self.assertEqual(node1, node4)
        
class TestConversion(unittest.TestCase):
    # Test case for converting TEXTNode to a HTMLNode, specifically a leaf node
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
        bold_node = TextNode("BOLD me daddy", TextType.BOLD)
        html_node_bold = text_node_to_html_node(bold_node)
        self.assertEqual(html_node_bold.tag, "b")
        self.assertEqual(html_node_bold.value, "BOLD me daddy")
        
        
        
        
if __name__ == "__main__":
    unittest.main()