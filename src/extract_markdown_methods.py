import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


# old nodes = list of TextNodes (text, text_type, url), return [TextNode(), TextNode()]
# text_type seems like will be TextType.TEXT
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not node.text_type == TextType.TEXT:
            new_nodes.append(node)
            continue

        current_text = node.text
        matches = extract_markdown_images(current_text)
        
        if not matches:
            new_nodes.append(node)
            continue

        for image_text, image_url in matches:
            fragment = f"![{image_text}]({image_url})"
            before, after = current_text.split(fragment, 1)
            
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            
            new_nodes.append(TextNode(image_text, TextType.IMAGE, image_url))
            
            # we are doing this because we want out AFTER to hold the text AFTER the first URL
            current_text = after
        
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        # will use regex to match and return a list of tuples that passed [("link", "https://boot.dev")]
        if not node.text_type == TextType.TEXT:
            new_nodes.append(node)
            continue
        
        current_text = node.text
        matches = extract_markdown_links(current_text)
        
        # if no links, keep node as it is
        if not matches:
            new_nodes.append(node)
            continue

        for link_text, link_url in matches:
            fragment = f"[{link_text}]({link_url})"
            # only 1 split with the fragment
            before, after = current_text.split(fragment, 1)
            
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            
            # we are setting the left over text to after because we want our
            # other links if it is in matches to go before it
            # [before, ----links----, after]
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            
            current_text = after
        
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes
