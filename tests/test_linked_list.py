import unittest

from datastruct.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        """Подготовка тестового односвязного списка"""
        self.linked_list = LinkedList()

    def test_empty_linked_list(self):
        """Проверка пустого односвязного списка"""
        self.assertEqual(self.linked_list.first_node, None)
        self.assertEqual(self.linked_list.last_node, None)

    def test_add_one_element_to_the_beginning(self):
        """Добавление одного элемента в начало односвязного списка"""
        self.linked_list.insert_beginning(data=1)

        self.assertEqual(self.linked_list.first_node.data, 1)
        self.assertEqual(self.linked_list.last_node.data, 1)
        self.assertEqual(str(self.linked_list), '1 -> None')

    def test_add_one_element_to_the_end(self):
        """Добавление одного элемента в конец односвязного списка"""
        self.linked_list.insert_at_end(data=1)

        self.assertEqual(self.linked_list.first_node.data, 1)
        self.assertEqual(self.linked_list.last_node.data, 1)
        self.assertEqual(str(self.linked_list), '1 -> None')

    def test_add_elements_to_the_beginning_and_end(self):
        """Добавление элементов в конец и в начало односвязного списка"""
        self.linked_list.insert_beginning({'id': 1})
        self.linked_list.insert_at_end({'id': 2})
        self.linked_list.insert_at_end({'id': 3})
        self.linked_list.insert_beginning({'id': 0})

        self.assertEqual(self.linked_list.first_node.data, {'id': 0})
        self.assertEqual(self.linked_list.first_node.next_node.data, {'id': 1})
        self.assertEqual(self.linked_list.last_node.data, {'id': 3})
        self.assertEqual(self.linked_list.last_node.next_node, None)
        self.assertEqual(str(self.linked_list), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")
