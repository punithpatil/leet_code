# https://leetcode.com/problems/binary-gap

class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        running_max = 0
        binary = bin(N)[2:]
        counter = 0
        for i in binary:
            if counter > running_max and i == "1":
                running_max = counter
            if i == "1":
                counter = 0
            counter += 1
            
        return running_max 
