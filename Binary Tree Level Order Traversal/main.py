# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
  Solution uses BFS to iterate the nodes of the binary tree.
  
  Time Complexity: O(n) where is the number of nodes in the binary tree.
  
  Solution iterates through each level of the binary tree, and appends the value of the current node to a temporary array which is used to store all the values
  of the nodes in the current level. Afterwards, the children of the current node are added to the queue to be visited next. We append the temporary array to our
  result array which should be an array of arrays containing the values of the levels. The temporary is initialized back to an empty array and we iterate through 
  the next level of nodes stored in our queue.
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root] if root else []
        res = []
        
        while(len(queue) > 0):

            currLevel = []
            for i in range(len(queue)):
                currNode = queue.pop(0)
                currLevel.append(currNode.val)
                
                if (currNode.left != None):
                    queue.append(currNode.left)
                if (currNode.right != None):
                    queue.append(currNode.right)
                
            res.append(currLevel)
            
        return res
