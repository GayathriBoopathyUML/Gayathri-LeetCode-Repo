from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # result=[]
        # c = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        # for i in c:
        #     if i[1] > (len(nums)//3):
        #         result.append(i[0])
        # return result
    
        threshold = len(nums) // 3
        return [num for num, count in Counter(nums).items() if count > threshold]
        