# Language
# avataryang913
# Back
# 376. Binary Tree Path Sum
# Description
# Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.
#
# A valid path is from root node to any of the leaf nodes.
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input:
# {1,2,4,2,3}
# 5
# Output: [[1, 2, 2],[1, 4]]
# Explanation:
# The tree is look like this:
# 	     1
# 	    / \
# 	   2   4
# 	  / \
# 	 2   3
# For sum = 5 , it is obviously 1 + 2 + 2 = 1 + 4 = 5
# Example 2:
#
# Input:
# {1,2,4,2,3}
# 3
# Output: []
# Explanation:
# The tree is look like this:
# 	     1
# 	    / \
# 	   2   4
# 	  / \
# 	 2   3
# Notice we need to find all paths from root node to leaf nodes.
# 1 + 2 + 2 = 5, 1 + 2 + 3 = 6, 1 + 4 = 5
# There is no one satisfying it.
# Related Problems
# Video Solution
# All video solutions
# 播放
# 376. 二叉树的路径和
# DifficultyEasy
# Total Accepted26578
# Total Submitted92047
# Accepted Rate28%
# Recommend Courses
# Web前端工程师P5~P6
# Web前端工程师P5~P6
# 7周快速掌握P5~P6前端知识体系，通过实战项目全面掌握求职面试的思路与技巧
#  Show Tags
# Leaderboard - Python3
#
# 离体的单细胞
# 870ms
#
# wanghaicheng
# Gold II
# 874ms
#
# yuzhi94
# 875ms
#
# LCUser_0X11DFB963C5EC5B7875
# 876ms
#
# AaronEver
# 876ms
# Note
# use `result.append(path.copy())` instead of `result.append(path)`
# avatarlingguang
# Created at a day ago
# 自己写的分治算法，还有待提高
# avatare2MxjR9Y8xaD
# Created at 4 days ago
# since it need to dfs left and right, how to back tracking if pass tmp by reference?
# avatarxu7963
# Created at 18 days ago
# Discuss
# augustulus7Bronze IV· Last reply by · Lili6 · 9 months ago
# name53· Last reply by · Lljie · a year ago
# gaosuwoniu2019· Last reply by · hao278004541 · 2 years ago
#   
# 376. Binary Tree Path Sum
# 中文English
# Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.
#
# A valid path is from root node to any of the leaf nodes.
#
# Example
# Example 1:
#
# Input:
# {1,2,4,2,3}
# 5
# Output: [[1, 2, 2],[1, 4]]
# Explanation:
# The tree is look like this:
# 	     1
# 	    / \
# 	   2   4
# 	  / \
# 	 2   3
# For sum = 5 , it is obviously 1 + 2 + 2 = 1 + 4 = 5
# Example 2:
#
# Input:
# {1,2,4,2,3}
# 3
# Output: []
# Explanation:
# The tree is look like this:
# 	     1
# 	    / \
# 	   2   4
# 	  / \
# 	 2   3
# Notice we need to find all paths from root node to leaf nodes.
# 1 + 2 + 2 = 5, 1 + 2 + 3 = 6, 1 + 4 = 5
# There is no one satisfying it.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root:
            return []
        total_results = []
        current_results = []
        self.sub_tree_sum(root, target, total_results, current_results)
        return total_results

    def sub_tree_sum(self, root, target, total_results, current_results):
        if root is None:
            return
        current_results.append(root.val)
        if root.left is None and root.right is None:
            if target == root.val:
                total_results.append(current_results)
            # del current_results[-1]
            return
        self.sub_tree_sum(root.left, target - root.val, total_results, current_results[:])
        self.sub_tree_sum(root.right, target - root.val, total_results, current_results[:])

        # del current_results[-1]

class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root:
            return []
        total_results = []
        current_results = []
        self.sub_tree_sum(root, target, total_results, current_results)
        return total_results

    def sub_tree_sum(self, root, target, total_results, current_results):
        if root is None:
            return
        current_results.append(root.val)
        if root.left is None and root.right is None:
            if target == root.val:
                total_results.append(current_results[:])
            del current_results[-1]
            return
        self.sub_tree_sum(root.left, target - root.val, total_results, current_results)
        self.sub_tree_sum(root.right, target - root.val, total_results, current_results)

        del current_results[-1]


# tips: list[:] is a copy of list. prevent all lists to be one memory address.
# tips: if not root
# tips: terminal condition: root is None.
# tips: can't use target < 0 return, maybe has negative number.






