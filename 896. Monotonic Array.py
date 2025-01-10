class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        valI = []
        valD = []
        for i in range(1,len(nums)):
            valI.append(nums[i-1]<=nums[i])
            valD.append(nums[i-1]>=nums[i])
        return(any([all(valI),all(valD)]))
                