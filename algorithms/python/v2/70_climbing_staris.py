# https://leetcode.com/problems/climbing-stairs/

# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n_1 value at n - 1
        # n_2 value at n - 2
        n_1 = 2
        n_2 = 1
        i = 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        for _ in range(n-2):
            i = n_1 + n_2
            n_2 = n_1
            n_1 = i 
            
        return i