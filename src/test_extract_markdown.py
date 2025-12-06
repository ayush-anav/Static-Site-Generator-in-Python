import unittest
from extract_markdown_methods import extract_markdown_images, extract_markdown_links

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