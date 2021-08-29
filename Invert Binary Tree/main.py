# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
  Solution uses BFS to iterate through the binary tree.
  
  Time Complexity: O(n) where n is the number of nodes in the binary tree.
  
  Initial guess was to iterate through the nodes of the binary tree and create a new tree where the nodes of the current level would be reversed.
  So if the current level consists of nodes [3,4,1,2], the new binary tree would have nodes of [2,1,4,2]. This would involve iterating through
  each current level. A better solution would be to visit each node and reverse their children. This is what the solution below does.
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root] if root else []
        
        while(len(queue) > 0):
            currNode = queue.pop(0)
            
            queueLeft = currNode.left
            queueRight = currNode.right
            
            currNode.left = queueRight
            currNode.right = queueLeft
            
            if (currNode.left != None):
                queue.append(currNode.left)
            if (currNode.right != None):
                queue.append(currNode.right)
            
        return root
        
