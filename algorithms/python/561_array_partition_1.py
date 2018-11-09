# https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        return sum(nums[::2])
