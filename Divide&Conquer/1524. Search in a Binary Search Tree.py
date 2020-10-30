# 1524. Search in a Binary Search Tree
# 中文English
# Given the root of a binary search tree (BST) and a value.
#
# Return the node whose value equals the given value. If such node doesn't exist, return null.
#
# Example
# Example 1:
#
# Input: value = 2
#         4
#        / \
#       2   7
#      / \
#     1   3
# Output: node 2
# Example 2:
#
# Input: value = 5
#         4
#        / \
#       2   7
#      / \
#     1   3
# Output: null


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """

    def searchBST(self, root, val):
        # Write your code here.

        if root is None:
            return None
        if root.val == val:
            return root

        result_left = self.searchBST(root.left, val)
        result_right = self.searchBST(root.right, val)

        if result_left is not None:
            return result_left   #
        if result_right is not None:
            return result_right   #!

        return None