from textnode import TextNode, TextType
import inspect
from htmlnode import HTMLNode

if __name__ == "__main__":
    example = HTMLNode("", "", "", {"href": "https://www.google.com", "target": "_blank",})
    print(example.props_to_html())
