# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         newA=[]
#         for i in arr2:
#             # print(arr1.count(i))
#             for _ in range(arr1.count(i)):
#                 newA.append(i) 

#         leftover = (list(set(arr1)-set(arr2)))
#         leftover.sort()
#         # print(leftover)
#         arr = newA + leftover
#         # print(newA)
#         return (arr)


from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        newA = []
        
        # Count occurrences of each element in arr1
        count_map = {num: 0 for num in arr1}
        for num in arr1:
            count_map[num] += 1

        # Add elements to newA based on arr2 order
        for num in arr2:
            if num in count_map:
                newA.extend([num] * count_map[num])
                del count_map[num]  # Remove from map once processed

        # Sort remaining elements and add to result
        leftover = sorted(count_map.keys())
        for num in leftover:
            newA.extend([num] * count_map[num])

        return newA
