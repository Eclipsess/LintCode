# Given a sorted (increasing order) array, Convert it to create a binary search tree with minimal height.
#
# Example
# Example 1:
#
# Input: []
# Output:  {}
# Explanation: The binary search tree is null
# Example 2:
#
# Input: [1,2,3,4,5,6,7]
# Output:  {4,2,6,1,3,5,7}
# Explanation:
# A binary search tree with minimal height.
#
#          4
#        /   \
#       2     6
#      / \    / \
#     1   3  5   7
#
#
# Notice
# There may exist multiple valid solutions, return any of them.

# """
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
# """


class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """

    def sortedArrayToBST(self, A):
        # write your code here

        result = self.createBST(A)

        return result

    def createBST(self, A):
        if len(A) == 0:
            return None
        if len(A) == 1:
            return TreeNode(A[0])

        m = (len(A) - 1) // 2
        left_tree = self.createBST(A[:m])
        right_tree = self.createBST(A[m + 1:])

        tmp_node = TreeNode(A[m])
        tmp_node.left = left_tree
        tmp_node.right = right_tree
        return tmp_node


