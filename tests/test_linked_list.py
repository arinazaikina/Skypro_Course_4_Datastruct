import contextlib
import io
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

    def test_to_list(self):
        """Проверка списка с данными, содержащимися в односвязном списке"""
        self.linked_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.linked_list.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.linked_list.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.linked_list.insert_beginning({'id': 0, 'username': 'serebro'})

        self.assertEqual(len(self.linked_list.to_list()), 4)

    def test_get_data_by_id_correct_data(self):
        """Проверка получения словаря по id, когда все данные в списке корректные"""
        self.linked_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.linked_list.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.linked_list.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.linked_list.insert_beginning({'id': 0, 'username': 'serebro'})

        self.assertEqual(self.linked_list.get_data_by_id(value_id=3), {'id': 3, 'username': 'mosh_s'})
        self.assertEqual(self.linked_list.get_data_by_id(value_id=4), None)

    def test_get_data_by_id_incorrect_data(self):
        """Проверка получения словаря по id, когда в списке есть некорректные данные"""
        self.linked_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.linked_list.insert_at_end('idusername')
        self.linked_list.insert_at_end([1, 2, 3])
        self.linked_list.insert_at_end({'id': 2, 'username': 'serebro'})

        self.assertEqual(self.linked_list.get_data_by_id(value_id=2), None)

        s = io.StringIO()
        with contextlib.redirect_stdout(s):
            self.linked_list.get_data_by_id(value_id=2)
        self.assertEqual(s.getvalue(), 'Данные не являются словарем или в словаре нет id.\n')
