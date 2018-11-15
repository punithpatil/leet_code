# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # March through the array, read value and mark that
        # index with the negative value
        for i in nums:
            val = abs(i) - 1
            nums[val] = - abs(nums[val])
            
        output = []
        
        # Positive values's index indicated missing element
        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i+1)
        
        return output

