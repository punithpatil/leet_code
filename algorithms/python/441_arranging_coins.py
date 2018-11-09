# https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        stacks = (1+math.floor(math.sqrt(1+8*n)))/2
        
        return math.floor(stacks - 1)
        
        
