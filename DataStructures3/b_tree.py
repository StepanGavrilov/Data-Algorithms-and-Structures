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

    def remove_node(self, index: int):
        # TODO search here !
        previous_node = None
        current_node = self.root
        while current_node:
            if index < current_node.index:
                previous_node = current_node
                current_node = current_node.left
                if index == current_node.index:
                    if current_node.left is not None and current_node.right is None:  # Если есть один потомок левый
                        previous_node.left = current_node.left
                        return
                    if current_node.right is not None and current_node.left is None:  # Если есть один потомок правый
                        previous_node.left = current_node.right
                        return
            if index > current_node.index:
                previous_node = current_node
                current_node = current_node.right
                if index == current_node.index:
                    if current_node.right is not None and current_node.left is None:  # Если есть один потомок правый
                        previous_node.right = current_node.right
                        return
                    if current_node.left is not None and current_node.right is None:  # Если есть один потомок левый
                        previous_node.right = current_node.left
                        return
                    if current_node.left is not None and current_node.right is not None:  # Есть оба ребёнка
                        return

    def get_max(self) -> Node:
        """Max index"""
        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node

    def get_min(self) -> Node:
        """Min index"""
        current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def show_tree(self):                
        print(self.root.index)
        print(self.root.right.index)
        print(self.root.right.right.index)
        print(self.root.right.right.left.index)


if __name__ == '__main__':
    bt = BinaryTree()

    bt.add(25)
    bt.add(30)
    bt.add(55)
    bt.add(45)

    print('index', bt.get_min())
    bt.show_tree()
