# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set = set(nums)  # Convert list to set for quick lookup
        count = 0
        temp = head

        while temp:
            if temp.val in nums_set and (temp.next is None or temp.next.val not in nums_set):
                count += 1
                print(temp.val, count)
            temp = temp.next
        
        return count
        