import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class Test_HTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "www.boot.dev", "target": "_blank"})
        expected_result = " href: www.boot.dev target: _blank"
        self.assertEqual(node.props_to_html(), expected_result)

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("<h1>", "Some title")
        expected_result = f"HTMLNode(<h1>, Some title, None, None)"
        self.assertEqual(repr(node), expected_result)

    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)

class Test_LeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "click me", {"href":"www.boot.dev"})
        expected_result = '<a href="www.boot.dev">click me</a>'
        self.assertEqual(node.to_html(), expected_result)

    def test_to_html_empty_value(self):
        node = LeafNode("a", None)
        self.assertRaises(ValueError, node.to_html)

class Test_ParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("p", [LeafNode("b", "bold text"), LeafNode(None, "normal text"), LeafNode("i", "italic Text")])
        self.assertEqual(node.to_html(), "<p><b>bold text</b>normal text<i>italic Text</i></p>")

    def test_to_html_with_props(self):
        node = ParentNode("p", [LeafNode("b", "bold text")], {"href": "www.boot.dev"})
        self.assertEqual(node.to_html(), '<p href="www.boot.dev"><b>bold text</b></p>')

    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("p", "some text")])
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_children(self):
        node = ParentNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_nested_parents(self):
        node = ParentNode("p", [ParentNode("b", [LeafNode("i", "bold and italic text")])])
        self.assertEqual(node.to_html(), f'<p><b><i>bold and italic text</i></b></p>')
        

if __name__ == "__main__":
    unittest.main()