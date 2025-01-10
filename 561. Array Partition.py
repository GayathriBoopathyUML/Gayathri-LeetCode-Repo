class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sort_num = sorted(nums)
        sum=0
        for i in range(1,len(sort_num),2):
            sum+=(min(sort_num[i-1],sort_num[i]))
        return sum
        