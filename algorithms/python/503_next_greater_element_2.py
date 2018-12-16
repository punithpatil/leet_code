# https://leetcode.com/problems/next-greater-element-ii/

# Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

# Example 1:

# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number; 
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.

class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        max_value_index = nums.index(max(nums))
        nums_length = len(nums)
        
        # Put indices inside of stack instead of actual numbers
        stack = []
        lookup = {}
        
        i = max_value_index + 1
        
        for _ in nums:
            real_index = i%nums_length
            if not stack:
                stack.append(real_index)
            elif nums[real_index] <= nums[stack[-1]]:
                stack.append(real_index)
            else:
                while stack and nums[real_index] > nums[stack[-1]]:
                    lookup[stack.pop()] = real_index
                stack.append(real_index)
            i += 1
        
        output = []
        for i in range(nums_length):
            try:
                output.append(nums[lookup[i]])
            except:
                output.append(-1)
                
        return output