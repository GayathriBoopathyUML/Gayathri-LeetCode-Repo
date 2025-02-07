class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = []
        for i in nums:
            result.append(sum(map(int, str(i))))
        return(min(result))
        