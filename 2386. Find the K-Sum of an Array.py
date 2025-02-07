class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        # # nums.sort()
        # result = [0]
        # for i in range(len(nums)):
        #     result.append(nums[i])
        #     for j in range(i+1,len(nums)):
        #         result.append(nums[i]+nums[j])
        #         if(j<len(nums)-1):
        #             result.append(nums[i]+sum(nums[j:]))
        # # print(result)
        # result.sort()
        # reverse = result[::-1]
        # return (reverse[k-1])
        lis=[]
        sumi=0
        t=[]
        for i in nums:
            if i>=0:
                sumi+=i
                t.append(-i)
            else:
                t.append(i)
        t.sort(reverse=True)
        t=t[:k+2]
        lis.append(sumi)
        for i in t:
            n=len(lis)
            for j in range(n):
                lis.append(i+lis[j])
            lis.sort(reverse=True)   
            if len(lis)>k:
                lis=lis[:k]
        # print(lis)
        return lis[k-1]  
        