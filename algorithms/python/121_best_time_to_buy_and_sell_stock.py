# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        import math
        running_min = next(iter(prices), None)
        running_max_profit = 0
        for i in prices:
            if i < running_min:
                running_min = i
            if i - running_min > running_max_profit:
                running_max_profit = i - running_min
                
        return running_max_profit
        
