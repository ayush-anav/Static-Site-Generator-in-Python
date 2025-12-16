from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_html_node(markdown):
    # converts full markdown doc -> single HTMLNode (it will have nesting)
    
    # md_blocks = returns a list of block elements
    md_blocks = markdown_to_blocks(markdown)
    
    # children of parent
    children = []
    
    for block in md_blocks:
        # returns BlockType Enum (code, p, h, quote, ul, l)
        block_type = block_to_block_type(block)
        # based on BlockType, create a new HTMLNode, helper func needed (sim to split_nodes_delimiter helper)
        child_node = create_html_node(block_type, block)
        children.append(child_node)
        
    return ParentNode("div", children)
    
    
def create_html_node(block_type, block):
    match block_type:
        case BlockType.HEADING:
            # determine what heading it is
            heading_no = determine_heading_count(block)
            # call text_to_textnode (for children)
            text = block[heading_no: ].strip()
            children = text_to_children(text)
            return ParentNode(f"h{heading_no}", children)
        
        case BlockType.CODE:
            lines = block.split("\n")
            inner_line = lines[1:-1]
            code_text = "\n".join(inner_line)
            
            text_node = TextNode(code_text, TextType.TEXT)
            code_leaf = text_node_to_html_node(text_node)
            
            code_node = ParentNode("code", [code_leaf])
            return ParentNode("pre", [code_node])  
              
        case BlockType.QUOTE:
            lines = block.split("\n")
            cleaned_lines = []
            
            for line in lines:
                cleaned_lines.append(line.lstrip(">").strip())
            
            text = " ".join(cleaned_lines)
            children = text_to_children(text)
            return ParentNode("blockquote", children)
        
        case BlockType.PARAGRAPH:
            lines = block.split("\n")
            text = " ".join(lines).strip()
            
            children = text_to_children(text)
            return ParentNode("p", children)

        case BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []
            
            for line in lines:
                # removes "- " (dash + space) for each element in unordered list
                # then it searches for any children (if exists)
                text = line[2:].strip()
                children = text_to_children(text)
                li_nodes.append(ParentNode("li", children))
            # then returns ParentNode with <ul> <li>NODE</li> </ul>
            return ParentNode("ul", li_nodes)
        
        case BlockType.ORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []
            
            for line in lines:
                # removes the "1. " (num + dot + space [3:]) 
                # then searches if child exist
                # if yes or no append to li_node
                text = line[3:].strip()
                children = text_to_children(text)
                li_nodes.append(ParentNode("li", children))
            
            return ParentNode("ol", li_nodes)


def determine_heading_count(block):
    count = 0
    while count < len(block) and block[count] == "#" and count < 6:
        count += 1
        # see if we need to handle count > 6
    return count

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children        
