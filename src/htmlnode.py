class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tage = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("")

    def props_to_html(self):
        prop_output = ""
        for prop in self.props:
            prop_output += f" {prop[0]}={prop[1]}"
        return prop_output


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if not self.value:
            if not self.value:
                raise ValueError("All leaf nodes must have a value.")
            if self.tag == None:
                return value
            return f"<{self.tag}>{self.value}</{self.tag}>"
