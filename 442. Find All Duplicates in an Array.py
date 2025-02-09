class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # return(list(set([i for i in nums if nums.count(i)>1])))
        seen = set()
        duplicates = set()

        for num in nums:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        
        return list(duplicates)