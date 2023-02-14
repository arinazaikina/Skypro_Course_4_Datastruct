class Node:
    """
    Базовый класс Узел
    Attrs:
        data: данные (любые полезные данныеЖ число, строка, список и т.д.)
        next_node: ссылка на следующий узел
    """

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    def __str__(self):
        return f'Node(data={self.__data}, next_node={self.__next_node})'

    def __repr__(self):
        return repr(f'Node(data={self.__data}, next_node={self.__next_node})')

    @property
    def data(self):
        """Геттер. Возвращает данные"""
        return self.__data

    @data.setter
    def data(self, data):
        """Сеттер. Устанавливает данные"""
        self.__data = data

    @property
    def next_node(self):
        """Геттер. Возвращает ссылку на следующий узел"""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """Сеттер. Устанавливает ссылку на следующий узел"""
        self.__next_node = next_node
