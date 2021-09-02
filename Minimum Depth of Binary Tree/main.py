# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = [root] if root else []
        level = 1 if root else 0
        
        while(len(queue) > 0):
            print(level, len(queue))
            for i in range(len(queue)):
                currNode = queue.pop(0)
                if currNode.left == None and currNode.right == None:
                    return level
                else:
                    if currNode.left != None:
                        queue.append(currNode.left)
                    if currNode.right != None:
                        queue.append(currNode.right)
            level += 1
        
        return level
