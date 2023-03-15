from typing import Any


class Node:
    """
    Базовый класс Узел
    Attrs:
        data: данные (любые полезные данные: число, строка, список и т.д.)
        next_node: ссылка на следующий узел
    """

    def __init__(self, data: Any, next_node=None) -> None:
        """
        Узел инициализируется данными и ссылкой на следующий узел.
        По умолчанию ссылка - None
        """
        self.__data = data
        self.__next_node = next_node

    def __str__(self) -> str:
        return f'Node(data={self.__data}, next_node={self.__next_node})'

    def __repr__(self) -> str:
        return repr(f'Node(data={self.__data}, next_node={self.__next_node})')

    @property
    def data(self) -> Any:
        """Геттер. Возвращает данные"""
        return self.__data

    @data.setter
    def data(self, data: Any) -> None:
        """Сеттер. Устанавливает данные"""
        self.__data = data

    @property
    def next_node(self) -> 'Node':
        """Геттер. Возвращает ссылку на следующий узел"""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node: 'Node') -> None:
        """Сеттер. Устанавливает ссылку на следующий узел"""
        self.__next_node = next_node
