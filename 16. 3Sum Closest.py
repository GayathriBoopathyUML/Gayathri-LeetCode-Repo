# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         if sum(nums) == target:
#             return len(nums)
#         if target in nums:
#             index=nums.index(target)
#             val=nums[index]
#             if index-1>0:
#                 val+=nums[index-1]
#             if index+1<len(nums):
#                 val+=nums[index+1]
#             return(val)
#         else:
#             if sum(nums) == target:
#                 return len(nums)
#             return 0


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')  # Initialize with a large number
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update the closest sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move the pointers to try and get a sum closer to the target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # If the exact sum is found, return it
        
        return closest_sum
