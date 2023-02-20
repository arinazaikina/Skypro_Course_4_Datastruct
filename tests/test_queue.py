import unittest

from datastruct.queue import Queue


class TestStack(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')

    def test_object_name(self):
        self.assertEqual(str(self.queue), 'data1 -> data2 -> data3 -> None')

    def test_queue(self):
        self.assertEqual(self.queue.head.data, 'data1')
        self.assertEqual(self.queue.head.next_node.data, 'data2')
        self.assertEqual(self.queue.tail.data, 'data3')
        self.assertEqual(self.queue.tail.next_node, None)
