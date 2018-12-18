# https://leetcode.com/problems/majority-element/

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore Voting Algorithm
        # https://en.wikipedia.org/wiki/Boyer–Moore_majority_vote_algorithm
        candidate = count = 0
        
        for i in nums:
            if count == 0:
                candidate = i
                count += 1
            elif candidate == i:
                count += 1
            else:
                count -= 1
        
        return candidate
        