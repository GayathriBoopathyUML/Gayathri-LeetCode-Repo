class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        # result=[]
        # for i in range(len(nums)):
        #     if nums[i]>0:
        #         result.append(nums[(i+nums[i])%(len(nums))])
        #     elif nums[i]<0:
        #         result.append(nums[i-abs(nums[i])])
        #     else:
        #         result.append(nums[i])
        # return result
        ans = []
        n = len(nums)
        for i, x in enumerate(nums):
            ans.append(nums[(i + x + n) % n] if x else 0)
        return ans
        