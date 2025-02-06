from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        result = 0
        count = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                p = nums[i]*nums[j]
                count[p] += 1
        # print(count)
        for i in count.values():
            if i>1:
                result += (i*(i-1)//2)*8
        return result
        