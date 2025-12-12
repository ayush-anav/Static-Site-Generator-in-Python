from textnode import TextType, TextNode
from split_delimiter import split_nodes_delimiter
from extract_markdown_methods import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    
    # all allowed delimiter
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # img and link
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes