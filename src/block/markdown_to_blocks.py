def markdown_to_blocks(markdown):
    # takes markdown string and returns BLOCK strings
    # block level elements
    supplied_markdown = markdown.split("\n\n")
    
    block_elements = []
    
    for element in supplied_markdown:
        stripped_elements = element.strip()
        if stripped_elements != "":
            block_elements.append(stripped_elements)
            
    return block_elements