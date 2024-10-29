#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitMax = 0
        buyPrice = prices[0]
        for sellPrice in prices[1::]:
            if buyPrice > sellPrice:
                buyPrice = sellPrice
            else:
                profitMax = max(profitMax, sellPrice-buyPrice)

        return profitMax
        
# @lc code=end

