# Given a binary tree, return all root-to-leaf paths.
#
# Example
# Example 1:
#
# Input：{1,2,3,#,5}
# Output：["1->2->5","1->3"]
# Explanation：
#    1
#  /   \
# 2     3
#  \
#   5
# Example 2:
#
# Input：{1,2}
# Output：["1->2"]
# Explanation：
#    1
#  /
# 2

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
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []
        current_path = ""
        total_paths = []
        self.traversal(root, total_paths, current_path)
        return total_paths

    def traversal(self, root, total_paths, current_path):
        if root is None:
            return
        current_path = '->'.join([current_path, str(root.val)])
        # current_path += (str(root.val) + "->")
        if root.left is None and root.right is None:
            current_path = current_path[2:]
            total_paths.append(current_path)
            return
        self.traversal(root.left, total_paths, current_path[:])
        self.traversal(root.right, total_paths, current_path[:])














