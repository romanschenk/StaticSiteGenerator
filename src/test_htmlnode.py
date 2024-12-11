import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()