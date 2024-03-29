from typing import Any

from datastruct.node import Node


class Queue:
    """
    Базовый класс Очередь
    """
    def __init__(self) -> None:
        """
        Очередь инициализируется пустой
        """
        self.__head = None
        self.__tail = None

    def __str__(self) -> str:
        result = ''
        current_node = self.__head
        while current_node is not None:
            result += str(current_node.data) + ' -> '
            current_node = current_node.next_node
        else:
            result += 'None'
        return result

    @property
    def head(self) -> Node:
        """Геттер. Возвращает первый узел очереди"""
        return self.__head

    @property
    def tail(self) -> Node:
        """Геттер. Возвращает последний узел очереди"""
        return self.__tail

    def enqueue(self, value: Any) -> None:
        """
        Добавляет данные в конец очереди.
        :param value: данные
        """
        new_node = Node(data=value)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next_node = new_node
            self.__tail = new_node

    def dequeue(self) -> Any:
        """
        Удаляет первый добавленный в очередь элемент и
        возвращает данные удалённого элемента.
        """
        if self.__head is None:
            return
        value = self.__head.data
        self.__head = self.__head.next_node
        return value