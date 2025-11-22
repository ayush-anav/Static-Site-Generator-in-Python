import unittest

from textnode import TextNode, TextType

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
        
if __name__ == "__main__":
    unittest.main()