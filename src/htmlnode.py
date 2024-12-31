

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if not type(self.props) == dict: return result
        for key in self.props.keys():
            result += f" {key}: {self.props[key]}"
        return result
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        elif self.tag is None:
            return self.value
        result = ["<", self.tag]
        if not self.props is None:
            for key in self.props.keys():
                result.append(f' {key}="{self.props[key]}"')
        result.append(f">{self.value}</{self.tag}>")
        return "".join(result)

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag: raise ValueError("Tag missing")
        if not self.children: raise ValueError("Children Missing")
        props_str = ""
        if self.props:
            for key in self.props.keys():
                props_str += f' {key}="{self.props[key]}"'
        result = f"<{self.tag + props_str}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result