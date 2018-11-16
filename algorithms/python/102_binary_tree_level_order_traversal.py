# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:

# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import collections
        
        levels = collections.defaultdict(list)
        
        height = 0
        
        def inorder(root):
            nonlocal height 
            
            if not root:
                return 
            
            levels[height].append(root.val)
            
            height += 1
            inorder(root.left)
            inorder(root.right)
            height -= 1
           
        inorder(root)
        
        output = []
        for key in levels:
            output.append(levels.get(key))

        return output