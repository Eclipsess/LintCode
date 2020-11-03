"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree
    """

    def trimBST(self, root, minimum, maximum):
        # write your code here
        if root is None:
            return root
        root = self.check_tree(root, minimum, maximum)

        return root

    def check_tree(self, root, minimum, maximum):

        if root is None:
            return None

        left = self.check_tree(root.left, minimum, maximum)
        right = self.check_tree(root.right, minimum, maximum)

        root.left = left
        root.right = right

        if root.val < minimum:
            return root.right
        if root.val > maximum:
            return root.left

        return root

