class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        for i in range(2**n):
            x=(format(i, f'0{n}b'))
            if x in nums:
                continue
            else:
                return(x)
        