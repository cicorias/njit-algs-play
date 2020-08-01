import unittest


class BSTNode:
    def __init__(self, key: int, left=None, right=None) -> None:
        self.key = key
        self.right = right
        self.left = left

    def print_tree(self):
        pass


    def get_array(self):
        pass


class BST:
    def __init__(self, root: BSTNode=None) -> None:
        self.root = root

