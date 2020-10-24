# Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.
#
# Example
# Example 1:
#
# Input:{1,2,2,4},{1,2,2,4}
# Output:true
# Explanation:
#         1                   1
#        / \                 / \
#       2   2   and         2   2
#      /                   /
#     4                   4
#
# are identical.
# Example 2:
#
# Input:{1,2,3,4},{1,2,3,#,4}
# Output:false
# Explanation:
#
#         1                  1
#        / \                / \
#       2   3   and        2   3
#      /                        \
#     4                          4
#
# are not identical.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """

    def isIdentical(self, a, b):
        # write your code here
        result = self.towRoot(a, b)
        return result

    def towRoot(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        result_left = self.towRoot(root1.left, root2.left)

        result_right = self.towRoot(root1.right, root2.right)

        return result_left and result_right