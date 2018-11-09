# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import OrderedDict
class Solution:
    
        
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        level = 0
        contents = OrderedDict()
        def helper(root,h):
            nonlocal contents
            if(root == None):
                return
            if h not in contents:
                contents[h] = [root.val]
            else:
                contents[h].append(root.val)
            helper(root.left,h+1)
            helper(root.right,h+1)
        
        helper(root,0)
        output = [sum(content)/len(content) for _, content in contents.items()]
        return output
        
    
        
        
        
