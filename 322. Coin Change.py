class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(len(dp)):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        return -1 if dp[-1] == float('inf') else dp[-1]

        # coins.sort(reverse=True)  # Ensure the coins are sorted
        # count = 0
        # i = 0  # Start with the largest coin

        # while amount > 0 and i < len(coins):
        #     count += amount // coins[i]  # Take as many of this coin as possible
        #     amount %= coins[i]  # Reduce amount
        #     i += 1  # Move to the next smallest coin

        # return count if amount == 0 else -1  # If amount is still > 0, return -1