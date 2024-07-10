class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newList = []
        for i in nums:
            if i not in newList:
                newList.append(i)
        for i in range(len(newList)):
            nums[i] = newList[i]
        return len(newList)
        