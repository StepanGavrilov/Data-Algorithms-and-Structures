class Node:

    def __init__(self, value, item):
        self.right = None
        self.left = None
        self.value = value  # индекс
        self.item = item


class BinaryTree:

    def __init__(self):
        self.root = None  # Вершина дерева

    def add(self, value, item=None):
        """Добавление нового Node"""
        if self.root is None:
            self.root = Node(value, item=item)
        else:
            if value < self.root.value:  # Если меньше root, то влево
                current_node = self.root
                while current_node:
                    if value < current_node.value:  # Если входной элемент меньше значения элемента левого поддерева
                        if current_node.left is not None:  # Спуск по дереву
                            current_node = current_node.left
                        else:
                            # Если нашли конечный Node
                            current_node.left = Node(value, item=item)
                            break
                    if value > current_node.value:
                        if current_node.right is not None:  # Если входной элемент больше значения элемента левого
                            # поддерева
                            current_node = current_node.right
                        else:
                            # Если нашли конечный Node
                            current_node.right = Node(value, item=item)
                            break
            if value > self.root.value:  # Если больше root, то вправо
                current_node = self.root
                while current_node:
                    if value > current_node.value:
                        if current_node.right is not None:  # Если есть в правом поддереве элементы, то спускаемся
                            current_node = current_node.right
                        else:
                            current_node.right = Node(value, item=item)  # Если есть в правом поддереве нашли конец
                            break
                    if value < current_node.value:
                        if current_node.left is not None:
                            current_node = current_node.left
                        else:
                            current_node.left = Node(value, item=item)
                            break

    def search(self, index: int):
        """Поиск элемента по индексу"""
        if index == self.root:
            return self.root
        current_node = self.root
        while current_node:
            if index < current_node.value:
                current_node = current_node.left
                if current_node is None:
                    raise IndexError('Non-existent index')
                if index == current_node.value:
                    return current_node
            if index > current_node.value:
                current_node = current_node.right
                if current_node is None:
                    raise IndexError('Non-existent index')
                if index == current_node.value:
                    return current_node

    def get_tree_height(self):
        pass

    def remove(self):
        pass

    def show_tree(self):
        print(self.root.value)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add(15)
    bt.add(10)
    bt.add(3)
    bt.add(1)
    bt.add(-4)
    bt.add(23)
    bt.add(231)

    bt.search(234)
