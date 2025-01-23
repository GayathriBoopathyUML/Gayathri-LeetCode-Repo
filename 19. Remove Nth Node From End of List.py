
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        first = second = dummy

        # Move first pointer n+1 steps ahead to maintain gap
        for _ in range(n + 1):
            first = first.next

        # Move first to the end, second will reach the (n+1)th node from end
        while first:
            print(first.val,second.val)
            first = first.next
            second = second.next

        # Remove the nth node from end
        second.next = second.next.next

        return dummy.next  # Return the updated head of the linked list
