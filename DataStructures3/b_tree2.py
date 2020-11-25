import random

from DataStructures3.tree_utils import TreeNode
from DataStructures3.tree_utils import pretty_print_tree
from queue import Queue


class BST:
    def __init__(self):
        self.root = None
        self.n = 0

    def insert(self, key, val=None):
        node = TreeNode(key, val)
        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, node)
        self.n += 1

    def _insert(self, root: TreeNode, node: TreeNode) -> None:
        """
        :Time: O(log(n))
        :Space: O(log(n))
        """
        if root is None:
            return

        if node.key < root.key:
            if root.left is None:
                root.left = node
            else:
                self._insert(root.left, node)

        elif node.key > root.key:
            if root.right is None:
                root.right = node
            else:
                self._insert(root.right, node)

    def get(self, key) -> TreeNode:
        ret_val = self._get(self.root, key)
        if ret_val is None:
            raise LookupError("Key Error!")
        else:
            return ret_val

    def _get(self, root: TreeNode, key: TreeNode) -> TreeNode:
        """
        :Time: O(log(N))
        :Space: O(log(N))
        """
        if root is None:
            return None

        if root.key == key:
            return root

        result_left_subtree = None
        result_right_subtree = None

        if key < root.key:
            result_left_subtree = self._get(root.left, key)
        elif key > root.key:
            result_right_subtree = self._get(root.right, key)

        if result_left_subtree is not None:
            return result_left_subtree
        elif result_right_subtree is not None:
            return result_right_subtree
        else:
            return None

    def contains(self, key) -> bool:
        """
        :Time: O(log(n))
        """
        bfs_queue = Queue()
        bfs_queue.put(self.root)
        while not bfs_queue.empty():
            removed = bfs_queue.get()
            if removed.key == key:
                return True

            if key < removed.key and removed.left is not None:
                bfs_queue.put(removed.left)  # mark visited
            if key > removed.key and removed.right is not None:
                bfs_queue.put(removed.right)  # mark visited
        return False

    def get_height(self) -> int:
        return self._get_height(self.root)

    def _get_height(self, root) -> int:
        """
        Algorithm: max(recur left, recur right) + 1
        """
        if root is None:
            return 0
        height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        return height

    def get_max(self):
        """
        :Time: O(N)
        :Space: O(1)
        :return: the maximum key in the tree
        """
        if self.root is None:
            return '-Inf'

        current = self.root
        while current.right is not None:
            current = current.right

        return current.key

    def get_min(self):
        if self.root is None:
            return '+Inf'

        current = self.root
        while current.left is not None:
            current = current.left

        return current.key

    def get_min_node(self, root: TreeNode) -> TreeNode:
        """
        :Time: O(N)
        :Space: O(1)
        :return: the minimum key node in the tree
        """
        if root is None:  # BC1
            return None

        current = root
        while current.left is not None:
            current = current.left

        return current

    def delete(self, key) -> TreeNode:
        def delete_helper(root: TreeNode, key) -> TreeNode:
            """
            :Time: O(log(n)) average
            :Space: O(log(n) average
            """
            if root is None:
                return None
            if key < root.key:
                new_root_left = delete_helper(root.left, key)
                root.left = new_root_left
            elif key > root.key:
                new_root_right = delete_helper(root.right, key)
                root.right = new_root_right
            else:
                if root.left is None and root.right is None:
                    return None
                elif root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    inorder_successor = self.get_min_node(root.right)
                    root.key, root.val = inorder_successor.key, inorder_successor.val
                    new_root_successor = delete_helper(root.right, inorder_successor.key)
                    root.right = new_root_successor
                    return root

            return root

        return delete_helper(self.root, key)


if __name__ == "__main__":

    tree = BST()

    tree.insert(50)
    tree.insert(51, val='Value')
    tree.insert(45, val='Value')
    tree.insert(15, val='Value')
    tree.insert(1, val='Value')

    pretty_print_tree(tree.root)

    tree.delete(50)

    pretty_print_tree(tree.root)
