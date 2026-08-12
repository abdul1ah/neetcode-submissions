# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_depth = 1

        if not root:
            return 0
        
        stack = [(root,max_depth)]

        
        while stack:
            curr , depth = stack.pop()

            if curr.left:
                stack.append((curr.left , depth+1))
            
            if curr.right:
                stack.append((curr.right , depth+1))

            max_depth = max(max_depth , depth)


        return max_depth
