# Python program to introduce Binary Tree
"""
           1
       /       \
      2          3
    /   \       /  \
   4     5    None None
  /  \
None None
"""


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def inorder(root):
    if root:
        inorder(root.left)
        print root.key
        inorder(root.right)

def preorder(root):
    if root:
        print root.key
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print root.key

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print 'runniing proorder\n'
preorder(root)

print 'running inorder\n'
inorder(root)

print 'running postorder\n'
postorder(root)
