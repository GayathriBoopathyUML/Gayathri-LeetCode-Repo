# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0  # Base case: empty tree has depth 0
        
        # If one of the children is missing, we must take the depth of the non-null child
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        
        # If both children exist, take the minimum of both depths
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        