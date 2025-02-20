class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            val = (sum(int(i) for i in str(i)))
            if val in dic:
                dic[val].append(i)
            else:
                dic[val] = [i]
        # print(dic)
        result = []
        t = []
        for total,arr in dic.items():
            if len(arr)>=2:
                arr.sort()
                s = int(sum([arr[-1],arr[-2]]))
                result.append(s)
            else:
                t.append(-1)
        result.sort()
        # print(result,t)
        if len(t)==len(nums):
            return -1
        else:
            return result[-1]
             
        