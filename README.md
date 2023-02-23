# Библиотека Datastruct
 Пакет, который позволяет другим программистам “из коробки” использовать различные структуры данных для эффективной организации работы с данными: их добавления, удаления, хранения и поиска.
 
 ## Задачи
 * Создать класс узла `Node`, содержащий два атрибута:
    - данные 
    (сюда будут записываться любые полезные данные: число, строка, список и т.д.)
    - ссылка на следующий узел
* Создать класс `Stack`, одноименной структуры данных. 
Экземпляр класса `Stack` инициализируется одним атрибутом, хранящим ссылку на верхний (крайний в стэке) узел. Для пустого стэка этот атрибут будет содержать `None`.
* Создать метод `push` для добавления данных в стэк. 
* Реализовать метод `pop()` класса `Stack`. Метод удаляет из стека верхний элемент (последний добавленный), реализуя правило LIFO (Last In, First Out) и возвращает данные удаленного экземпляра класса `Node`.
* Создать класс `Queue`, одноименной структуры данных. Экземпляр класса `Queue` инициализируется двумя атрибутами, хранящими ссылки на начало и конец очереди. Для пустой очереди оба эти атрибута равны `None`.
* Создать метод `enqueue` для добавления данных в очередь. 
