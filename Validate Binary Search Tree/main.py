# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
  Recursion Solution
  
  Time Complexity: O(n) where n is the number of nodes in the tree
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode], greaterThan = None, lessThan = None) -> bool:
           
        isValid = True
        if (root == None):
            return isValid
        if (greaterThan != None and root.val <= greaterThan):
            isValid = False
        if (lessThan != None and root.val >= lessThan):
            isValid = False

        return isValid and self.isValidBST(root.left, greaterThan, root.val) and self.isValidBST(root.right, root.val, lessThan)
        
