# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        if k == 0:
            return 0

        if k > len(prices) // 2:
            profit = 0
            for i in range(1, 1+len(prices[1:])):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit

        buy = [float('-inf') for _ in range(k)]
        sell = [0 for _ in range(k)]

        buy[0] = float('-inf')
        for currPrice in prices:
            buy[0] = max(buy[0], -currPrice)
            sell[0] =max(sell[0], buy[0] + currPrice)
            for j in range(1, k):
                buy[j] = max( buy[j], -currPrice + sell[j-1] )
                sell[j] = max(sell[j], currPrice + buy[j])

        return sell[k-1]

print(Solution().maxProfit(4, [1,2,4,2,5,7,2,4,9,0]))

