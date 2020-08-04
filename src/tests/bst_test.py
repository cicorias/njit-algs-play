import unittest

from src.algs.trees.BST import BST, BSTNode

class Test_Bst(unittest.TestCase):
    def setUp(self) -> None:
        self.root = BSTNode(4)

# '''
#         4
#        / \
#       /   \
#      2     6
#     / \   / \
#    1   3 5   7

# '''
    def make_tree(self) -> BSTNode:
        root = BSTNode(4)
        root.left = BSTNode(2)
        root.right = BSTNode(6)
        root.left.left = BSTNode(1)
        root.left.right = BSTNode(3)
        root.right.left = BSTNode(5)
        root.right.right = BSTNode(7)

        return root

    def test_get_array(self):
        node = self.make_tree()
        bst = BST()
        exp = [1, 2, 3, 4, 5, 6, 7]
        act = bst.get_array(node)
        act2 = bst.makeList(node)
        act3 = bst.makeList2(node)
        self.assertListEqual(exp, act, 'get array failed')

    def test_bst_print(self):
        node = self.make_tree()
        bst = BST()
        # bst.printLevelOrder(node)
        self.assertEqual(bst.height(node), 3)


if __name__ == "__main__":
    unittest.main()