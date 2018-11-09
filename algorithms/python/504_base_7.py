# https://leetcode.com/problems/base-7/

class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        digits = []
        negative_flag = False
        if num == 0:
            digits.append("0")
        elif num<0:
            negative_flag = True
        else:
            negative_flag = False
        num = abs(num)
        while num:
            digits.append(str(num%7))
            num //= 7
        
        if negative_flag:
            digits.append("-")
            
        return "".join(digits[::-1])
        
