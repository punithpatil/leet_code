# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Given a binary tree, flatten it to a linked list in-place.

# For example, given the following tree:

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        while root:
            if root.left:
                left_child = left_head = root.left
                while left_child.right:
                    left_child = left_child.right
                if root.right:
                    left_child.right = root.right
                root.left = None
                root.right = left_head
            root = root.right
        
        