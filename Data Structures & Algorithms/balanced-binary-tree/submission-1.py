# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced=True
        
        def dfs(root):
            nonlocal isBalanced

            if root is None:
                return 0

            right_depth=dfs(root.right)
            left_depth=dfs(root.left)

            if abs(left_depth - right_depth) > 1:
                isBalanced=False

            return 1+max(left_depth,right_depth)

        dfs(root)
        return isBalanced
