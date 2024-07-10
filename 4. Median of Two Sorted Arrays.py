class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newArray = nums1 + nums2
        newArray.sort()
        if len(newArray)%2 == 0:
            return (newArray[int(len(newArray)/2)] + newArray[int(len(newArray)/2 -1)])/2
        else:
            return newArray[int(len(newArray)/2)]