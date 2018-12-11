# https://leetcode.com/problems/first-unique-character-in-a-string/

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """        
        import collections
        
        char_freq = collections.Counter(s)
        
        index = 0
        for ch in s:
            if char_freq[ch] == 1:
                return index
            index += 1
            
        return -1