# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = r = head
        while r and r.next:
            l = l.next
            r = r.next.next
        prev = None
        while l:
            nextNode = l.next
            l.next = prev
            prev = l
            l = nextNode
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True