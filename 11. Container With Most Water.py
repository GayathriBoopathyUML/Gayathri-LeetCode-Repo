# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         value = []
#         for i in range(len(height)):
#             for j in range(i, len(height)):
#                 if i != j:
#                     value.append(min(height[i], height[j]) * max((j-i), (i-j)))
#                     # value.append([min(height[i], height[j]),max((j-i), (i-j))])
#         # print(max(value))
#         return(max(value))
        
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
