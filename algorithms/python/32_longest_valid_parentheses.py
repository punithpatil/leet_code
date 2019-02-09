# https://leetcode.com/problems/longest-valid-parentheses/

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

class Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        stack = []
        
        stack.append(-1)
        result = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    result = max(result, i - stack[-1])
                else:
                    stack.append(i)
        return result
                    