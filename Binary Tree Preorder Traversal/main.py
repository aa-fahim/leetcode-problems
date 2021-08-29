# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
  Solution uses DFS and pre-order traversal to iterate through the binary tree.
  
  Time Complexity: O(n) where n is the number of nodes in the binary tree.
  
  Notes:
  The solution appends the right child node first then the left child node of the current node. This is because we are utilizing a stack data structure which operates
  on a LIFO basis. Since the question asks us to iterate through the tree in a pre-order traversal manner, we want to first visit the left child node then the right
  child node.
'''
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root] if root else []
        res = []
        
        while(len(stack) > 0):
            currNode = stack.pop(-1)
            res.append(currNode.val)    
            if (currNode.right != None):
                stack.append(currNode.right)
            if (currNode.left != None):
                stack.append(currNode.left)
        
        return res
    
        
                
            
        
        
