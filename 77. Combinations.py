from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # nums = [i for i in range(1,n+1)]
        nums = list(range(1, n + 1))  # Generate numbers from 1 to n
        return list(map(list, combinations(nums, k)))  # Convert tuples to lists
        