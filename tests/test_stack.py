import unittest

from datastruct.node import Node

from datastruct.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')

    def test_object_name(self):
        self.assertEqual(str(self.stack), 'data2 -> data1 -> None')

    def test_push(self):
        self.assertEqual(self.stack.top.data, 'data2')
        self.assertEqual(self.stack.top.next_node.data, 'data1')
        self.assertEqual(self.stack.top.next_node.next_node, None)

    def test_set_top(self):
        self.stack.top = Node('data')
        self.assertEqual(str(self.stack), 'data -> None')
