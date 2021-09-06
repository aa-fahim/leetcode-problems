# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
  Approach
  First traversal of the linked list, grab all values of nodes and store in temporary array.
  Second traversal of the linked list, replace the value of the current node with either the first or last element of the array. After replacing value
  of node, remove the element from the array.
  
  Time Complexity: O(2*n) where n is the number of nodes in the linked list
  
  Alternative Appraoch
  Use slow and fast pointer to determine middle of linked list.
  Traverse through middle until end of linked list and reverse this part of the linked list and store into a temporary variable.
  Traverse through the full linked list and merge the first half of the linked list with the reversed second half.
  
  Time Complexity: O(n) where n is the number of nodes in the linked list.
  
  
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        arrValues = []
        currNode = head
        
        while(currNode != None):
            arrValues.append(currNode.val)
            currNode = currNode.next

        tmp = 0
        currNode = head
        while(len(arrValues) > 0):
            val = arrValues.pop(tmp)
            currNode.val = val
            currNode = currNode.next
            
            if tmp == 0:
                tmp = -1
            else:
                tmp = 0
        return head
            
        
