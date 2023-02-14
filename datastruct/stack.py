from datastruct.node import Node

class Stack:
    """
    Базовый класс, описывающий Стэк
    Attrs:
        top: ссылка на верхний (крайний в стэке) узел
    """
    def __init__(self):
        self.__top = None

    def __str__(self):
        result = ''
        current_node = self.__top
        while current_node is not None:
            result += str(current_node.data) + ' -> '
            current_node = current_node.next_node
        else:
            result += 'None'
        return result

    @property
    def top(self):
        """Геттер. Возвращает ссылку на верхний узел"""
        return self.__top

    @top.setter
    def top(self, top):
        """Сеттер. Устанавливает ссылку на верхний узел"""
        self.__top = top

    def push(self, value) -> None:
        """
        Добавляет данные в стек
        :param value: данные
        """
        new_node = Node(data=value)
        new_node.next_node = self.top
        self.__top = new_node
