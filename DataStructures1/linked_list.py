class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.linked_list_len = 0

    def contains(self, value):
        """Проверяет наличие элемента в списке"""
        current_element = self.head
        while current_element:
            if value == current_element:
                return True
            else:
                current_element = current_element.next_element
        return False

    def append_element(self, value):
        """Добавляет элемент в конец списка"""
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current_element = self.head
        while current_element.next_element:
            current_element = current_element.next_element
        current_element.next_element = node

    def get_element(self, index: int):
        """Получает элемент по индексу"""
        current_element = self.head
        counter_index = 0
        while counter_index != index:
            counter_index += 1
            current_element = current_element.next_element
        return current_element.value

    def get_linked_list_len(self) -> int:
        """Возвразает длину списка"""
        current_element = self.head
        while current_element:
            self.linked_list_len += 1
            current_element = current_element.next_element
        return self.linked_list_len

    def show_linked_list(self):
        """Выводит содержание списка"""
        storage = ''
        current_element = self.head
        while current_element:
            storage += str(current_element.value) + ' ---> '
            current_element = current_element.next_element
        print(storage)

    def pop_element(self):
        """Удаляет последний элемент списка"""
        index = self.get_linked_list_len() - 1
        current_element = self.head
        while current_element:
            index -= 1
            if index == 0:
                current_element.next_element = None
            current_element = current_element.next_element

    def insert_element(self, value, element_index: int):
        counter_index = 0
        current_element = self.head
        while current_element:
            counter_index += 1
            if counter_index == element_index:
                nxt_element = current_element.next_element
                new_element = Node(value)
                current_element.next_element = new_element
                new_element.next_element = nxt_element
            current_element = current_element.next_element


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append_element(1)
    linked_list.append_element(2)
    linked_list.append_element(3)
    linked_list.append_element(4)
    linked_list.append_element(5)
    linked_list.insert_element(100, 2)
    linked_list.show_linked_list()