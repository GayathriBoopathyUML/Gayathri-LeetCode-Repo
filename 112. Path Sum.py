# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False  # If the tree is empty, there's no path sum

        # If it's a leaf node, check if the remaining sum equals the node value
        if not root.left and not root.right:
            return root.val == targetSum

        # Recursively check the left and right subtrees with updated targetSum
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))