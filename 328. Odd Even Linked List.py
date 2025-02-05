# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # No rearrangement needed for 0 or 1 node
        
        odd = head  # Points to first odd-indexed node
        even = head.next  # Points to first even-indexed node
        even_head = even  # Store the head of even nodes
        
        while even and even.next:
            odd.next = even.next  # Link odd node to the next odd node
            odd = odd.next  # Move odd pointer
            
            even.next = odd.next  # Link even node to the next even node
            even = even.next  # Move even pointer
        
        odd.next = even_head  # Attach the even list at the end of the odd list
        
        return head  # Return the modified list
        