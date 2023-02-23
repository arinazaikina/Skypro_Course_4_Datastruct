from typing import Any

from datastruct.node import Node


class Stack:
    """
    Базовый класс, описывающий Стэк
    Attrs:
        top: ссылка на верхний (крайний в стэке) узел
    """

    def __init__(self) -> None:
        """Стэк инициализируется пустым"""
        self.__top = None

    def __str__(self) -> str:
        result = ''
        current_node = self.__top
        while current_node is not None:
            result += str(current_node.data) + ' -> '
            current_node = current_node.next_node
        else:
            result += 'None'
        return result

    @property
    def top(self) -> Node:
        """Геттер. Возвращает ссылку на верхний узел"""
        return self.__top

    @top.setter
    def top(self, top: Node) -> None:
        """Сеттер. Устанавливает ссылку на верхний узел"""
        self.__top = top

    def push(self, value: Any) -> None:
        """
        Добавляет данные в стек
        :param value: данные
        """
        new_node = Node(data=value)
        new_node.next_node = self.top
        self.__top = new_node

    def pop(self) -> Any:
        """
        Удаляет из стэка верхний элемент (последний добавленный) и возвращает данные
        удалённого элемента
        """
        if self.__top is None:
            return
        value = self.__top.data
        self.__top = self.__top.next_node
        return value
