from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_size = 0
        
        for i in range(len(nums)):
            count = 0
            while nums[i] != -1:  
                nums[i], i = -1, nums[i]
                count += 1
            
            max_size = max(max_size, count)
        
        return max_size
