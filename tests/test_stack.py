import unittest

from datastruct.node import Node

from datastruct.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        """Подготовка тестового стэка"""
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')

    def test_object_name(self):
        """Проверка отображения информации об объекте Stack для пользователя"""
        self.assertEqual(str(self.stack), 'data2 -> data1 -> None')

    def test_push(self):
        """Проверка получения данных из узлов стэка"""
        self.assertEqual(self.stack.top.data, 'data2')
        self.assertEqual(self.stack.top.next_node.data, 'data1')
        self.assertEqual(self.stack.top.next_node.next_node, None)

    def test_set_top(self):
        """Проверка установки одного узла в стэк"""
        self.stack.top = Node('data')
        self.assertEqual(str(self.stack), 'data -> None')


class TestStackPop(unittest.TestCase):
    """Тестирование метода pop"""
    def setUp(self):
        """Подготовка тестового стэка"""
        self.stack = Stack()
        self.stack.push('data1')

    def test_pop_with_one_node(self):
        """Проверка удаления узла из стэка, состоящего из одного узла"""
        data = self.stack.pop()
        self.assertEqual(self.stack.top, None)
        self.assertEqual(data, 'data1')

    def test_pop_with_two_nodes(self):
        """Проверка удаления узла из стэка, состоящего из двух узлов"""
        self.stack.push('data2')
        data = self.stack.pop()
        self.assertEqual(self.stack.top.data, 'data1')
        self.assertEqual(data, 'data2')

    def test_pop_empty_stack(self):
        """Проверка удаления узла из пустого стэка"""
        self.stack.pop()
        data = self.stack.pop()
        self.assertEqual(data, None)
