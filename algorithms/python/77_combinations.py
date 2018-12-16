# https://leetcode.com/problems/combinations/

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# Example:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        output = []
        
        def combinations(start_index, selected, k):
            nonlocal output, n
            if k == 0:
                output.append(selected)
            for i in range(start_index, n):
                combinations(i+1, selected+[i+1], k -1)
                
        combinations(0, [], k)    
          
        return output