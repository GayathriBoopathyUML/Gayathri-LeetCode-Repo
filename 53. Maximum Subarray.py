class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0
        maxsum = float('-inf')
        n = len(nums)
        for i in range(n):
            currsum += nums[i]
            # print(currsum,maxsum)
            maxsum = max(maxsum,currsum)
            if currsum <0:
                currsum = 0
        return(maxsum)
        