# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = head
        newL =[]
        while temp:
            newL.append(temp.val)
            temp=temp.next
        newL.sort()
        newNode = ListNode()
        current = newNode
        for i in newL:
            current.next = ListNode(i)
            current = current.next
        return newNode.next
        



# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head

#         # Step 1: Split the list into two halves
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
        
#         mid = slow.next
#         slow.next = None  # Break the list into two parts

#         # Step 2: Recursively sort both halves
#         left = self.sortList(head)
#         right = self.sortList(mid)

#         # Step 3: Merge two sorted halves
#         return self.merge(left, right)

#     def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         current = dummy

#         while l1 and l2:
#             if l1.val < l2.val:
#                 current.next = l1
#                 l1 = l1.next
#             else:
#                 current.next = l2
#                 l2 = l2.next
#             current = current.next

#         current.next = l1 if l1 else l2  # Append remaining elements
#         return dummy.next
