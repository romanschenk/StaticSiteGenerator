import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a test node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a test node", TextType.BOLD_TEXT, "www.boot.dev")
        node2 = TextNode("This is a test node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a test node", TextType.ITALIC_TEXT, "www.boot.dev")
        expected_result = "TextNode(This is a test node, italic, www.boot.dev)"
        self.assertEqual(repr(node), expected_result)



if __name__ == "__main__":
    unittest.main()