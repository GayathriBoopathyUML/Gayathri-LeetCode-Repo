from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return(list(map(list, set(permutations(nums))))) # Convert to a set to remove duplicates
