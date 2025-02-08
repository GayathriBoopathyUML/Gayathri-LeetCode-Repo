class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     result = []
    #     if len(prices) <=1:
    #         return 0
    #     for i in range(len(prices)):
    #         for j in range(i+1,len(prices)):
    #             result.append(prices[j]-prices[i])
    #     r = max(result)
    #     if(r >= 0):
    #         return r
    #     else:
    #         return 0
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Track the minimum price so far
        max_profit = 0  # Track the maximum profit

        for price in prices:
            if price < min_price:
                min_price = price  # Update minimum price
            else:
                max_profit = max(max_profit, price - min_price)  # Calculate profit

        return max_profit