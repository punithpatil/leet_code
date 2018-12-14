# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example, given a 3-ary tree:

# https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png 



 

# We should return its level order traversal:

# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
 

# Note:

# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        import collections
        levels = collections.defaultdict(list)
        
        def dfs(root, height):
            if not root:
                return 
            levels[height] += [root.val]
            for child in root.children:
                dfs(child, height + 1)
        
        dfs(root, 0)
        
        return [level for height, level in levels.items()]
        