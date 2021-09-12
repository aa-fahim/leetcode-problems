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

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        if left.val != right.val:
            return False
        
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
'''

'''
  Time Complexity: O(n) where n is the number of nodes in the tree.
  
  Iterative Approach
  The recursive approach basically uses a stack to check which left and right nodes to check next. So in iterative approach, we will manage our own stack.
  Popping the latest nodes in our stack and checking if the values are the same then we append the right of the left node and left of the right node to the stack 
  as a pair and also the left of the left node and right of the right node as a pair too.
  
'''

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: 
        res = True
        stack = [[root.left, root.right]] if root else []
        
        while len(stack) > 0:
            left, right = stack.pop(-1)
            
            if not left and not right:
                continue
            
            if not left or not right:
                res = False
                break
                
            if left.val != right.val:
                res = False
                break
                
            stack.append([left.left, right.right])
            stack.append([left.right, right.left])
            
        return res
            
        
