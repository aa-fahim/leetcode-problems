# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxLen = 0
        
        def helper(node):
            if node == None:
                return 0
            leftSide = helper(node.left)
            rightSide = helper(node.right)
            if leftSide + rightSide > self.maxLen:
                self.maxLen = leftSide + rightSide
            return max(leftSide, rightSide) + 1
        
        helper(root)
        return self.maxLen
