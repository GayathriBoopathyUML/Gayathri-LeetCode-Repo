# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return True  # Cycle detected
            
            visited.add(current)  # Store the node reference
            current = current.next
        
        return False  # No cycle
