import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("Test node", TextType.ITALIC, "www.blah.com")
        node2 = TextNode("Test node", TextType.BOLD, "www.blah.com")
        self.assertNotEqual(node, node2)

    def test_nourl(self):
        node = TextNode("Test node", TextType.ITALIC)
        self.assertIsInstance(node, TextNode)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()
