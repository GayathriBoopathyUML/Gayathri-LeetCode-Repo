class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # if len(nums)<=1:
        #     return nums
        # odd=[]
        # even=[]
        # for i in nums:
        #     if i%2==0:
        #         even.append(i)
        #     else:
        #         odd.append(i)
        # return even+odd


        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                # Swap the odd and even numbers
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 == 1:
                right -= 1
        return nums
        