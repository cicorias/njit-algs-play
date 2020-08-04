from __future__ import annotations


class BSTNode:
    def __init__(self, key: int, left: BSTNode = None, right: BSTNode = None) -> None:
        self._key = key
        self._right = right
        self._left = left

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, n: BSTNode):
        self._left = n

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, n: BSTNode):
        self._right = n

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, v: int):
        self.key = v


class BST:
    def __init__(self, root: BSTNode = None) -> None:
        self.root = root

    def print_tree(self):
        pass

    def makeList(self, T: BSTNode, a=[]):
        if T != None:
            self.makeList(T.left, a)
            a += [T.key]
            self.makeList(T.right, a)
        return a

    def makeList2(self, T: BSTNode):
        if T is None:
            return []
        return self.makeList2(T.left) + [T.key] + self.makeList2(T.right)

    def get_array(self, T: BSTNode, a = []):
        if T is None:
            return
        
        self.get_array(T.left, a)
        a += [T.key]
        self.get_array(T.right, a)

        return a

    # Function to  print level order traversal of tree
    def printLevelOrder(self, root):
        h = self.height(root)
        for i in range(1, h+1):
            self.printGivenLevel(root, i)

    # Print nodes at a given level

# https://stackoverflow.com/a/56864291/140618
    def printGivenLevel(self, root, level):
        if root is None:
            return
        if level == 1:
            print("{}".format(root.key)),
        elif level > 1:
            self.printGivenLevel(root.left, level-1)
            self.printGivenLevel(root.right, level-1)

    def height(self, node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            # Use the larger one
            if lheight > rheight:
                return lheight+1
            else:
                return rheight+1
