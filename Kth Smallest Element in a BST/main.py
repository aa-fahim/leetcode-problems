# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
            Inorder Traversal Approach
        '''
        current = root
        stack = []
        arr = []
        
        while(True):
            if current is not None:
                stack.append(current)
                current = current.left
            elif(len(stack) > 0):
                current = stack.pop(-1)
                arr.append(current.val)
                current = current.right
            else:
                break
        
        return arr[k-1]
 
