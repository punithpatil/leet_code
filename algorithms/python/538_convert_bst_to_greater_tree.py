# https://leetcode.com/problems/convert-bst-to-greater-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        running_sum = 0
        
        def reverse_in_order(root):
            nonlocal running_sum
            if root == None:
                return 0
            reverse_in_order(root.right)
            running_sum += root.val
            root.val = running_sum
            reverse_in_order(root.left)
        
        reverse_in_order(root)
        
        return root
            
