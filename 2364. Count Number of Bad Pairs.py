from collections import defaultdict
class Solution:
    # def countBadPairs(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     count = 0
    #     for i in range(n):
    #         for j in range(1,n):
    #             if i<j and j-i != nums[j]-nums[i]:
    #                 count+=1
    #                 # count.append([i,j])
    #     return(count)
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2  # Total (i, j) pairs
        freq_map = defaultdict(int)
        good_pairs = 0

        for i in range(n):
            key = nums[i] - i
            good_pairs += freq_map[key]  # Count pairs with same (nums[i] - i)
            freq_map[key] += 1  # Update count

        return total_pairs - good_pairs  # Bad pairs = total - good

            