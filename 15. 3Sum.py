# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         new_list = set()  
#         n = len(nums)

#         if n < 3:
#             return []

#         for i in range(n):
#             for j in range(i + 1, n):
#                 for k in range(j + 1, n):  
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         new_list.add(tuple(sorted([nums[i], nums[j], nums[k]])))  

#         return [list(triplet) for triplet in new_list]  


class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    out = []

    for i, n in enumerate(nums):
      if n > 0: break
      if i > 0 and n == nums[i-1]: continue

      l, r = i+1, len(nums) - 1

      while l < r: 
        threeSum = n + nums[l] + nums[r]

        if threeSum < 0:
          l += 1
        elif threeSum > 0:
          r -= 1
        else:
          out.append([n, nums[l], nums[r]])
          l += 1
          r -= 1

          while nums[l] == nums[l-1] and l < r:
            l += 1
  
          while nums[r] == nums[r+1] and l < r:
            r -= 1
    
    return out