# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_a = int(a,2)
        int_b = int(b,2)
        
        a_plus_b = int_a + int_b
        
        return "{0:b}".format(a_plus_b)
        
