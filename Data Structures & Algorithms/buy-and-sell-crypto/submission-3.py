class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        sell = 1
        while buy < sell and sell < len(prices):
            max_profit = max(prices[sell] - prices[buy], max_profit)
            if sell == len(prices)-1:
                buy += 1
                sell = buy+1
                continue
            sell += 1    
        return max_profit