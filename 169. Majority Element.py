from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if count == 0:
                x=n
            count += 1 if x==n else -1
        return(x)
        # c = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        # return(c[0][0])

        