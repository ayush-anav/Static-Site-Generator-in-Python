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