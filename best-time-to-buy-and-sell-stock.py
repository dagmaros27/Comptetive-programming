class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force 
        # maxDiff = 0
        # for i in range(len(prices)): #buying day
        #     for j in range(i+1,len(prices)): #selling fay
        #         maxDiff = max(maxDiff, prices[j] - prices[i])
        # return maxDiff

        l  =0
        max_profit = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit
