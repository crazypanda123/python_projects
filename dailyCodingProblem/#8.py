"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""


class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    count = 0
    def count_unival(self):
        curr_node = self
        while curr_node:
            if curr_node.left is None and curr_node.right is None:
                self.count += 1
            elif curr_node.left is None and curr_node.right is not None:
                curr_node.right.count_unival()
            elif curr_node.right is None and curr_node.left is not None:
                curr_node.left.count_unival()
            elif curr_node.left.key == curr_node.right.key:
                self.count += 1
                curr_node.left.count_unival()
                curr_node.right.count_unival()
        return self.count


root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(1)
