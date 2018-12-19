# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# 103. Binary Tree Zigzag Level Order Traversal
# Medium

# 697

# 47

# Favorite

# Share
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:

# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import collections
        levels = collections.defaultdict(list)
        def dfs(root, height):
            if not root:
                return None
            
            levels[height] += [root.val]
            dfs(root.left, height + 1)
            dfs(root.right, height +1)
        
        dfs(root, 0)
        
        output = []
        for key, item in levels.items():
            if key%2 == 0:
                output.append(item)
            else:
                output.append(item[::-1])
                
        return output