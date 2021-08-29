# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution uses BFS algorithm to iterate through the binary tree. 
# Time complexity: O(n) where n is the number of nodes in the tree.

# Solution uses a queue to determine which node to iterate through next. And another queue to hold the depth level of the next node to iterate through next. 
# This inefficiency can be improved by insteading of creating a queue to hold the depth level, we only increment the depth level once every node in the current
# node has been visited. This solution would include a for loop inside the while loop to iterate through every node in the current level and add all their children
# in the queue. Once all the nodes in the current have been visited, we increment the depth level counter and proceed to iterate through the nodes of the next level.

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        queue = []
        queueContainingLevels = []
        
        if (root != None):
            queue.append(root)
        queueContainingLevels.append({ "level": 1 })

        maxLevel = 0
        while (len(queue) > 0):
            currentNode = queue.pop(0)
            currentNodeWithLevel = queueContainingLevels.pop(0)

            if (currentNodeWithLevel["level"] > maxLevel):
                maxLevel = currentNodeWithLevel["level"]
            
            if currentNode.left != None:
                queue.append(currentNode.left)
                queueContainingLevels.append({ "level": (currentNodeWithLevel["level"] + 1)})
            if currentNode.right != None:
                queue.append(currentNode.right)
                queueContainingLevels.append({ "level": (currentNodeWithLevel["level"] + 1)})
                
        return maxLevel
        
