# 482. Binary Tree Level Sum
# English
# Given a binary tree and an integer which is the depth of the target level.
#
# Calculate the sum of the nodes in the target level.
#
# Example
# Example 1:
#
# Input：{1,2,3,4,5,6,7,#,#,8,#,#,#,#,9},2
# Output：5
# Explanation：
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
#    /       \
#   8         9
# 2+3=5
# Example 2:
#
# Input：{1,2,3,4,5,6,7,#,#,8,#,#,#,#,9},3
# Output：22
# Explanation：
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
#    /       \
#   8         9
# 4+5+6+7=22

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """

    def levelSum(self, root, level):
        # write your code here
        if not root:
            return 0
        result = 0
        result = self.sum_level_node(root, 1, level, result)
        return result

    def sum_level_node(self, root, current_level, target_level, result):
        if root is None:
            return result
        if current_level == target_level:
            if root != '#':
                result += root.val
            return result

        result = self.sum_level_node(root.left, current_level + 1, target_level, result)
        result = self.sum_level_node(root.right, current_level + 1, target_level, result)

        return result

# tips: every return return the result.
# tips: if root is None, return result.
#



