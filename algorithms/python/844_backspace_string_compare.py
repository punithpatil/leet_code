# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_stack  = []
        t_stack = []
        
        for i in S:
            if i != '#':
                s_stack.append(i)
            else:
                if s_stack:
                    s_stack.pop()
        for i in T:
            if i != '#':
                t_stack.append(i)
            else:
                if t_stack:
                    t_stack.pop()
                    
        if "".join(s_stack[::-1]) == "".join(t_stack[::-1]):
            return True
        else:
            return False
            
                
        
