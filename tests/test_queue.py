import unittest

from datastruct.queue import Queue


class TestStack(unittest.TestCase):
    def setUp(self):
        """Подготовка тестовой очереди"""
        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')

    def test_object_name(self):
        """Проверка отображения информации об объекте Queue для пользователя"""
        self.assertEqual(str(self.queue), 'data1 -> data2 -> data3 -> None')

    def test_queue(self):
        """Проверка получения данных из узлов очереди"""
        self.assertEqual(self.queue.head.data, 'data1')
        self.assertEqual(self.queue.head.next_node.data, 'data2')
        self.assertEqual(self.queue.tail.data, 'data3')
        self.assertEqual(self.queue.tail.next_node, None)

    def test_dequeue(self):
        """Проверка удаления элементов из очереди"""
        self.assertEqual(self.queue.dequeue(), 'data1')
        self.assertEqual(self.queue.dequeue(), 'data2')
        self.assertEqual(self.queue.dequeue(), 'data3')
        self.assertEqual(self.queue.dequeue(), None)
