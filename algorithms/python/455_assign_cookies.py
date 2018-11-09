# https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        
        i = j = 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                count += 1
                i+=1
                j+=1
            else:
                i+=1
                
        return count
