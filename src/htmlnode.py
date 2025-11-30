class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        # HTML tag name e.g p, a, h1
        self.tag = tag
        
        # value = what is inside the tag
        self.value = value
        
        # children = list(HTMLNode objects)
        self.children = children
        
        # props = k,v => attr, val
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        link = ""
        for attr, val in self.props.items():
            link += f' {attr}="{val}"'

        return link
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


# use keyword arguments, exclude children, that will default to None
# for props (optional), include default as None

class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):
        
        # children = hard coded to None, and we using keyword args.
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        # renders leaf node as string
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        
        # if no tag e.g <p> --- </p> just return text
        if not self.tag:
            return self.value
        
        # render HTML tag
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag not supplied")
        if not self.children:
            raise ValueError("ParentNode NEEDS at least 1 child.")
        
        inner_html = ""
        for child in self.children:
            inner_html += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"