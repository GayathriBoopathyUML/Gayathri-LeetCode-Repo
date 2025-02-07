# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  # Already sorted if empty or single node

        dummy = ListNode(0)  # Dummy node as new sorted list head
        current = head

        while current:
            prev = dummy  # Pointer to traverse sorted list
            next_node = current.next  # Store next node before inserting

            # Find correct position in sorted list
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert the node
            current.next = prev.next
            prev.next = current

            # Move to the next node
            current = next_node
        
        return dummy.next  # Return the sorted list