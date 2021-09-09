# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
  Time Complexity: O(h * l) where h is the height of tree and l is the number of leaves in the tree.
'''
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if (root == None):
            return res
        
        def traversePath(node, path):
            tmp = path + [node.val]
            if node.left == None and node.right == None:
                if sum(tmp) == targetSum:
                    res.append(tmp)
                    
            if (node.left != None):
                traversePath(node.left, tmp)
            if (node.right != None):
                traversePath(node.right, tmp)

        traversePath(root, [])
        
        return res
        
