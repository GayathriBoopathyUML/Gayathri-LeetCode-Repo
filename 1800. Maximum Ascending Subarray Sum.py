class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        newA = []
        nums.append(0)
        count=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                count+=nums[i]
            else:
                newA.append(count)
                count = nums[i]
        return (max(newA))



        