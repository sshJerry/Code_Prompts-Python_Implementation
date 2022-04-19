
"""
Runtime: 1074 ms, faster than 88.37% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 87.33% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, l, r = 0, 0, 1
        if len(prices) <= 1:
            return maxProfit
        while r<len(prices):
            temp = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
            else:
                maxProfit = temp if temp > maxProfit else maxProfit
            r += 1
        return maxProfit
