# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import math
        running_min = math.inf
        running_val = math.inf
        def in_order_abs_diff(root):
            nonlocal running_min, running_val
            if root == None:
                return 0
            in_order_abs_diff(root.left)
            if abs(root.val - running_val) < running_min:
                running_min = abs(root.val - running_val)
            running_val = root.val
            in_order_abs_diff(root.right)
            
        in_order_abs_diff(root)
        
        return running_min
                
