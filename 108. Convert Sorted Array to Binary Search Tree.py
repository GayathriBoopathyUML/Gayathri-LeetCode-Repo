# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None  # Base case: Empty list returns None
        
        mid = len(nums) // 2  # Find middle element
        root = TreeNode(nums[mid])  # Middle element becomes root
        
        # Recursively build left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])  # Left half
        root.right = self.sortedArrayToBST(nums[mid+1:])  # Right half
        
        return root  # Return the root of the BST
        