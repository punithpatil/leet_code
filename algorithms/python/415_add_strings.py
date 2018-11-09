# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = j = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        step = 0
        output = []
        while i < len(num1) and j < len(num2):
            step = int(num1[i]) + int(num2[j]) + carry
            digit = step%10
            carry = step//10
            output.append(digit)
            i += 1
            j += 1
            
        while i < len(num1):
            step = int(num1[i]) + carry
            digit = step%10
            carry = step//10
            output.append(digit)
            i += 1
            
        while j < len(num2):
            step = int(num2[j]) + carry
            digit = step%10
            carry = step//10
            output.append(digit)
            j += 1
            
        if carry != 0:
            output.append(carry)
        
        return "".join([str(digit) for digit in output][::-1])
