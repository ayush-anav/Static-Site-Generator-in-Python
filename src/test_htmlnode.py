import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_method(self):
        expected_res = ' href="https://www.google.com" target="_blank"'
        check = HTMLNode("a", "", "", { "href": "https://www.google.com", "target": "_blank" })

        self.assertEqual(check.props_to_html(), expected_res)