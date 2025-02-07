class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        n = len(nums)
        result = []
        # print(nums)

        for i in range(n - 3):  # Step 2: First loop for the first number
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate first elements
                continue
            for j in range(i + 1, n - 2):  # Step 3: Second loop for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate second elements
                    continue
                
                left, right = j + 1, n - 1  # Step 4: Two-pointer search for the last two numbers
                # print(nums[i],nums[j],nums[left],nums[right])
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:  # Step 5: Found a valid quadruplet
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # Step 6: Skip duplicate third and fourth elements
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    
                    elif total < target:  # Move left pointer forward if sum is too small
                        left += 1
                    else:  # Move right pointer backward if sum is too large
                        right -= 1

        return result  # Step 7: Return the list of quadruplets
        