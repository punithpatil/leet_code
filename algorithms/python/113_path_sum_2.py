# https://leetcode.com/problems/path-sum-ii/submissions/

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = []
        output = []
        def dfs(root, current_sum):
            nonlocal sum, stack, output
            if root:
                stack.append(root.val)
                if root.left is None and root.right is None:
                    if current_sum == sum:
                        output.append([*stack])
                if root.left:
                    dfs(root.left, current_sum + root.left.val)
                    stack.pop()
                if root.right:
                    dfs(root.right, current_sum + root.right.val)
                    stack.pop()
        
        dfs(root, root.val)
        
        return output
                    