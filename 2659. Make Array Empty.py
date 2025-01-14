# class Solution:
#     def countOperationsToEmptyArray(self, nums):
#         count = 0
#         while len(nums) > 0:
#             if min(nums) == nums[0]:
#                 nums.pop(0)
#             else:
#                 new_nums = nums[1:]
#                 new_nums.append(nums[0])
#                 nums = new_nums
#             count+=1
#             # print(new_nums,count)
#         return count

class Solution:
  def countOperationsToEmptyArray(self, nums: list[int]) -> int:
    n = len(nums)
    ans = n
    numToIndex = {}

    for i, num in enumerate(nums):
      numToIndex[num] = i

    nums.sort()

    for i in range(1, n):
      # On the i-th step we've already removed the i - 1 smallest numbers and
      # can ignore them. If an element nums[i] has smaller index in origin
      # array than nums[i - 1], we should rotate the whole left array n - i
      # times to set nums[i] element on the first position.
      if numToIndex[nums[i]] < numToIndex[nums[i - 1]]:
        ans += n - i

    return ans