class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        beforeLeft = dummy
        
        # Move beforeLeft to the node before 'left'
        for _ in range(left - 1):
            beforeLeft = beforeLeft.next
        
        # Reverse sublist between left and right
        prev = None
        current = beforeLeft.next
        for _ in range(right - left + 1):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        # Reconnect the reversed sublist
        beforeLeft.next.next = current  # Connect tail of reversed sublist to afterRight
        beforeLeft.next = prev  # Connect beforeLeft to new head of reversed sublist
        
        return dummy.next  # Return new head (handles edge case when left == 1)