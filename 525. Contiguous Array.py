# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         new = [int(x) if x != '0' else -1 for x in map(str, nums)]
        
#         L = [[len(new[i:j]) for i in range(len(new)) for j in range(i + 1, len(new) + 1) if sum(new[i:j]) == 0]]        
#         Z = sum(L, [])  # Flatten list

#         return max(Z) if Z else 0  # Handle empty case safely

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {0: -1}  # Stores (count → first index)
        count = 0
        max_length = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1  # Replace 0 with -1 while calculating sum
            
            if count in count_map:
                max_length = max(max_length, i - count_map[count])
            else:
                count_map[count] = i  # Store first occurrence of count
        
        return max_length