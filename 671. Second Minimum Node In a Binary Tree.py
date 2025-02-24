# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        # result = set()
        # result.add(root.val)
        # def solve(root):
        #     if root is None:
        #         return []
        #     result.add(solve(root.left))
        #     result.add(solve(root.right))
        # solve(root)
        # return result[-2]

        if root is None:
            return -1  # No second minimum if tree is empty

        unique_values = set()

        def dfs(node):
            if node:
                unique_values.add(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        min_val = root.val
        second_min = float('inf')

        for val in unique_values:
            if min_val < val < second_min:
                second_min = val

        return second_min if second_min < float('inf') else -1
        