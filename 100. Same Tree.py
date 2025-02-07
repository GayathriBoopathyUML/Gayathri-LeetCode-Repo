# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def order(node1, node2):
            if node1 is None and node2 is None:
                return True  # Both are None, so they're the same
            if node1 is None or node2 is None:
                return False  # One is None, the other is not
            
            if node1.val != node2.val:
                return False  # Values differ, not the same tree
            
            # Recursively check left and right subtrees
            return order(node1.left, node2.left) and order(node1.right, node2.right)
        
        return order(p, q)
        
        