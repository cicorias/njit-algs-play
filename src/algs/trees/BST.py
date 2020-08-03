from __future__ import annotations


class BSTNode:
    def __init__(self, key: int, left: BSTNode=None, right: BSTNode= None) -> None:
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

