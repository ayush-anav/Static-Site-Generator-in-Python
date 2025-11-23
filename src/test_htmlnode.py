import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_method(self):
        expected_res = ' href="https://www.google.com" target="_blank"'
        check = HTMLNode("a", "", "", { "href": "https://www.google.com", "target": "_blank" })

        self.assertEqual(check.props_to_html(), expected_res)
        
    def test_node_render(self):
        node_p = LeafNode("p", "This is a paragraph of text.").to_html()
        self.assertEqual(node_p, "<p>This is a paragraph of text.</p>")
        
        node_a = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(node_a, '<a href="https://www.google.com">Click me!</a>')