# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         p = ListNode(0,head)
#         listN = p
#         while listN:
#             if listN and listN.next and listN.next.val and listN.next.val == listN.val:
#                 # print(listN.val)
#                 val = listN.next.val  # Store duplicate value
#                 while listN.next and listN.next.val == val:  # Skip all occurrences
#                     listN.next = listN.next.next
#                 # listN.next = listN.next.next
#             else:
#                 # print(listN.val,"%")
#                 listN = listN.next
#         return p.next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Remove all duplicates from a sorted linked list such that 
        each element appears only once and return the modified list."""
      
        # Initialize current to point to the head of the list
        current = head
      
        # Traverse the linked list
        while current and current.next:
            # If the current value is equal to the value in the next node
            if current.val == current.next.val:
                # Bypass the next node as it's a duplicate
                current.next = current.next.next
            else:
                # Move to the next unique value if no duplicate is found
                current = current.next
              
        # Return the head of the updated list
        return head