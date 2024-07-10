class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        element_index = dict()
        return_list = []
        for i in range(len(nums)):
            val = nums[i]
            reqd_num = target - val
            if reqd_num in element_index.keys():
                return_list = [i, element_index[reqd_num]]
            element_index[val] = i

        # newList=[]
        # length = len(nums)
        # for i in range(length):
        #     # print(i)
        #     value1 = nums[i]
        #     for j in range(i+1, length):
        #         value2 = nums[j]
        #         if value1 + value2 == target:
        #             return [i, j]
            # value=nums[int(nums.index(i))+1,int(len(nums))-1]
            # print(nums.index(i)+1, len(nums)-1)
            # for j in value:
            #     if i+j==target:
            #         newList=[i,j]
        return return_list