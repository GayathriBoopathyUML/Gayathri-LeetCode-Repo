# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def order(root):
            if root is None:
                return 0
            l = order(root.left)
            r = order(root.right)

            if l == -1 or r == -1 or abs(l-r)>1:
                return -1
            return max(l,r)+1
        
        return (order(root) != -1)

        # def checkHeight(root):
        #     if root is None:
        #         return 0  # Base case: empty tree has height 0
            
        #     left_height = checkHeight(root.left)
        #     right_height = checkHeight(root.right)
            
        #     if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
        #         return -1  # Return -1 if tree is unbalanced
            
        #     return max(left_height, right_height) + 1  # Return the height of current node
        
        # return checkHeight(root) != -1  # Tree is balanced if we never return -1