from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
            
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception("invalid md")

        tmp_list = []
        for i in range(len(parts)):
            if i % 2 == 0:
                # for index 0 and 2 it will be TextType.TEXT
                tmp_list.append(TextNode(parts[i], TextType.TEXT))
            else:
                # index 1 will be have text_type
                tmp_list.append(TextNode(parts[i], text_type))
                
        new_list.extend(tmp_list)
    return new_list