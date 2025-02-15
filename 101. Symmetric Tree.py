# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def order(node1, node2):
            if node1 is None and node2 is None:
                return True  # Both are None, symmetric
            if node1 is None or node2 is None:
                return False  # One is None but the other isn't, asymmetric
            if node1.val != node2.val:
                return False  # Values don't match, asymmetric
            
            # Recursively check mirrored positions
            return order(node1.left, node2.right) and order(node1.right, node2.left)
        
        return order(root.left, root.right)