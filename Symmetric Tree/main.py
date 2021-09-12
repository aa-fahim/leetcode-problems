# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
  Time Complexity: O(n) where n is the number of nodes in the tree.
  
  Recursion Approach
  Make sure left of left node is equal to right of right node and that right of left node and left of right node is the same.
'''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if not left and not right:
            return True
        
        if (not left and right) or (left and not right):
            return False
        
        if left.val != right.val:
            return False
        
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
            
        
