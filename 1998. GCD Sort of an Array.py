import math
class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > nums[j] and math.gcd(nums[i], nums[j]) != 1:
        #             nums[i],nums[j] = nums[j],nums[i]
        # print(nums)
        
        max_num = max(nums)
        
        # Step 1: Union-Find initialization
        parent = list(range(max_num + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX  # Union operation

        # Step 2: Connect numbers based on GCD > 1
        for num in nums:
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    union(num, factor)  # Connect num with its smallest prime factor
                    union(num, num // factor)  # Connect num with another divisor

        # Step 3: Compare sorted and original positions
        sorted_nums = sorted(nums)
        for original, sorted_val in zip(nums, sorted_nums):
            if find(original) != find(sorted_val):  
                return False  # Sorting is not possible within connected groups

        return True
        