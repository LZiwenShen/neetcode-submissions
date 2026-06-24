class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        mx = 0
        for sell in range(1, len(prices)):
            if prices[sell] > prices[buy]:
                cur = prices[sell] - prices[buy]
                mx = max(mx, cur)
            else:
                buy = sell
        return mx
