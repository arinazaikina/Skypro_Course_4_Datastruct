from typing import Any

from datastruct.node import Node


class LinkedList:
    """Базовый класс Связанный список"""
    def __init__(self):
        """Односвязный список инициализируется пустым"""
        self.__first_node = None
        self.__last_node = None

    def __str__(self) -> str:
        result = ''
        current_node = self.__first_node
        while current_node is not None:
            result += str(current_node.data) + ' -> '
            current_node = current_node.next_node
        else:
            result += 'None'
        return result

    @property
    def first_node(self) -> Node:
        """Геттер. Возвращает первый узел односвязного списка"""
        return self.__first_node

    @property
    def last_node(self) -> Node:
        """Геттер. Возвращает последний узел односвязного списка"""
        return self.__last_node

    def insert_beginning(self, data) -> None:
        """
        Добавляет данные в начало односвязного списка.
        :param data: данные
        """
        new_node = Node(data=data)
        if self.__first_node is None:
            self.__first_node = new_node
            self.__last_node = new_node
        else:
            new_node.next_node = self.__first_node
            self.__first_node = new_node

    def insert_at_end(self, data) -> None:
        """
        Добавляет данные в конец односвязного списка.
        :param data: данные
        """
        new_node = Node(data=data)
        if self.__first_node is None:
            self.__first_node = new_node
            self.__last_node = new_node
        else:
            self.__last_node.next_node = new_node
            self.__last_node = new_node
