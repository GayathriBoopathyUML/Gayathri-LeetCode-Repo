# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def order(node):
            if node is None:
                return
            # print(node.val)
            result.append(node.val)
            order(node.left)
            order(node.right)
        order(root)
        return(result)
        