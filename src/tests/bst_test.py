import unittest

from src.algs.trees.BST import BSTNode

class Test_Bst(unittest.TestCase):
    def setUp(self) -> None:
        self.root = BSTNode(4)


    def make_tree(self):
        root = BSTNode(4)
        

    def test_one(self):
        vi = 1 + 1
        self.assertEqual(vi, 2)
