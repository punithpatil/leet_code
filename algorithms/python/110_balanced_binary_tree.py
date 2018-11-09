# https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def helper(root):
            if root == None:
                return 0
                
            left = helper(root.left)
            right = helper(root.right)
            if left == -1 or right == -1:
                return -1
            elif abs(left - right) > 1:
                return -1
            else:
                return max(left,right)+1
                    
        return helper(root) != -1
