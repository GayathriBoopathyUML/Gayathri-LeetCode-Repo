from collections import Counter
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        result = Counter(nums)
        nums.sort()
        val = list(result.values())
        val.sort()
        if val[-1] >= 3:
            return False
        else:
            return True
        