from DataStructures3.tree_utils import TreeNode
from DataStructures3.tree_utils import pretty_print_tree
from DataStructures3.b_tree2 import BST


class AVLTreeNode(TreeNode):
    def __init__(self, key, val=None, bf=0):
        super().__init__(key, val)
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.bf = bf  # Balance
        self.height = 1  # Height


class AVLTree(BST):
    def __init__(self):
        super().__init__()

    def insert(self, key, val=None):
        self.root = self._insert(self.root, key, val)
        self.n += 1

    def _insert(self, root: AVLTreeNode, key, val=None) -> AVLTreeNode:
        if not root:
            return AVLTreeNode(key, val, bf=0)
        if key < root.key:
            left_sub_root = self._insert(root.left, key, val)
            root.left = left_sub_root
            left_sub_root.parent = root
        elif key > root.key:
            right_sub_root = self._insert(root.right, key, val)
            root.right = right_sub_root
            right_sub_root.parent = root
        else:
            return root  # duplicates
        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.bf = self._get_height(root.left) - self._get_height(root.right)
        return self.rebalance(root)  # re-balance

    def rebalance(self, root: AVLTreeNode) -> AVLTreeNode:
        """
        4 cases:
        1) bf(root) = 2 and bf(root.left) < 0 ==> L-R Imbalance
        2) bf(root) = 2 ==> L-L Imbalance
        3) bf(root) = -2 and bf(root.right) > 0 ==> R-L Imbalance
        4) bf(root) = -2 ==> R-R Imbalance
        """
        if root.bf == 2:
            if root.left.bf < 0:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
            else:  # L-L
                return self.rotate_right(root)
        elif root.bf == -2:
            if root.right.bf > 0:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
            else:  # R-R
                return self.rotate_left(root)
        else:
            return root  # no re-balance

    def rotate_right(self, root: AVLTreeNode) -> AVLTreeNode:
        """
        :Time: O(1)
        :Space: O(1)
        """
        pivot = root.left
        tmp = pivot.right
        # Кидаем правого ребёнка в корень и обновляем указатели родителя
        pivot.right = root
        pivot.parent = root.parent
        root.parent = pivot
        root.left = tmp
        if tmp:
            tmp.parent = root

        # Обновляем центр
        if pivot.parent:
            if pivot.parent.left == root:
                pivot.parent.left = pivot  # Если есть новый ребёнок
            else:
                pivot.parent.right = pivot  # наоборот, только для правого

        # Обновляем высоту и балагс
        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.bf = self._get_height(root.left) - self._get_height(root.right)
        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1
        pivot.bf = self._get_height(pivot.left) - self._get_height(pivot.right)
        return pivot  # новый корень

    def rotate_left(self, root: AVLTreeNode) -> AVLTreeNode:
        """
        :Time: O(1)
        :Space: O(1)
        :return: root of updated tree.
        """
        pivot = root.right
        tmp = pivot.left

        pivot.left = root
        pivot.parent = root.parent
        root.parent = pivot

        root.right = tmp
        if tmp:
            tmp.parent = root

        if pivot.parent:
            if pivot.parent.left == root:
                pivot.parent.left = pivot
            else:
                pivot.parent.right = pivot
        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.bf = self._get_height(root.left) - self._get_height(root.right)
        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1
        pivot.bf = self._get_height(pivot.left) - self._get_height(pivot.right)
        return pivot

    def _get_height(self, root: AVLTreeNode) -> int:
        if not root:  # 0 высота
            return 0
        else:
            return root.height


if __name__ == '__main__':
    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(15)
    avl_tree.insert(12)
    avl_tree.insert(8)
    avl_tree.insert(3)
    avl_tree.insert(5)
    avl_tree.insert(1)
    avl_tree.insert(-2)
    avl_tree.insert(-3)
    avl_tree.insert(-12)

    pretty_print_tree(avl_tree.root)

    avl_tree.delete(-12)

    pretty_print_tree(avl_tree.root)
