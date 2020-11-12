from DataStructures3.btree_print import print_btree


class Node:

    def __init__(self, index, item):
        self.right = None
        self.left = None
        self.index = index
        self.item = item


class BinaryTree:

    def __init__(self):
        self.root = None  # Вершина дерева

    def add(self, index, item=None):
        """Добавление нового Node"""
        if self.root is None:
            self.root = Node(index, item=item)
        else:
            current_node = self.root
            while current_node:
                if index < current_node.index:
                    if current_node.left is None:
                        current_node.left = Node(index, item=item)
                        break
                    current_node = current_node.left
                if index > current_node.index:
                    if current_node.right is None:
                        current_node.right = Node(index, item=item)
                        break
                    current_node = current_node.right

    def search(self, index: int):
        """Поиск элемента по индексу"""
        if index == self.root:
            return self.root
        current_node = self.root
        while current_node:
            if index < current_node.index:
                current_node = current_node.left
                if current_node is None:
                    raise IndexError('Non-existent index')
                if index == current_node.index:
                    return current_node
            if index > current_node.index:
                current_node = current_node.right
                if current_node is None:
                    raise IndexError('Non-existent index')
                if index == current_node.index:
                    return current_node

    def get_tree_height(self):
        pass

    def remove(self):
        pass

    def show_tree(self):
        pass


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add(25)
    bt.add(20)
    bt.add(17)
    bt.add(1, 'yeah')
    bt.add(15)
    bt.add(35)
    bt.add(34)
    bt.add(45)
    bt.add(44)
    bt.add(60)

    bt.show_tree()
