# 1534. Convert Binary Search Tree to Sorted Doubly Linked List

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """

    def treeToDoublyList(self, root):
        # Write your code here.
        if root is None:
            return root
        self.prev = None
        self.first = None
        self.inorder(root)
        self.first.left = self.prev
        self.prev.right = self.first
        return self.first

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        if self.first == None:
            self.first = root
        if self.prev == None:
            self.prev = root
        else:
            self.prev.right = root
            root.left = self.prev
        self.prev = root
        self.inorder(root.right)

# inorder
# record the previous node and combine it to be doubly linked list.