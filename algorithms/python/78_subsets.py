# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = set()
        def helper(n):
            nonlocal output
            if not n or tuple(n) in output:
                return 
            for i in range(len(n)):
                temp = n[0:i] + n[i+1:]
                helper(temp)
                output.add(tuple(n))
          
        helper(nums)  
        subsets = [*list(output),[]]
        return subsets
