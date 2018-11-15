# https://leetcode.com/problems/binary-number-with-alternating-bits

# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

# Example 1:

# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
# Example 2:

# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
# Example 3:

# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
# Example 4:

# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.
# Accepted
# 31,891
# Submissions
# 56,184

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # XOR with n and n-1 should result in all `1`s in the binary representation 
        n ^= n>>1
        return False if n&(n+1) else True # now AND with n+1 should result in 0