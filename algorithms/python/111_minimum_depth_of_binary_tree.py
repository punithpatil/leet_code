# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import math
        min_height = math.inf
        if not root:
            return 0
        
        def dfs(root, height):
            nonlocal min_height
            if root:
                if root.left is None and root.right is None:
                    if height < min_height:
                        min_height = height
                    return
                dfs(root.left, height + 1)
                dfs(root.right, height + 1)

        dfs(root, 1)
        return min_height
            
            