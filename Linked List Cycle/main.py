# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
  Time Complexity: O(n) where n is the number of nodes in the linked list.
  
  Solution uses an iterative approach to visit every node in the linked list.
  
  We append the memory location of the nodes to a hash table to track which nodes we have visited. We check if the current node's memory location is in the hash 
  hash table. If it is, then it means we have visited that node already. If it is not, then we append the memory location to our hash table and proceed to the
  next node.
'''

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visitedValues = []
        
        currNode = head
        res = False
        while(currNode != None):
            if (id(currNode) not in visitedValues):
                visitedValues.append(id(currNode))
                currNode = currNode.next
            else:
                res = True
                break
                
        return res
