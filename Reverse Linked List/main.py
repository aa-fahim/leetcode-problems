# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
  Time Complexity: O(n) where n is the number of nodes in the linked list.
  
  Solution uses iterative approach to visit every node in the linked list and append it to a new linked list.
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return ListNode(val='')
        
        res = ListNode()
        tempNode = head
        
        while(True):
            res.val = tempNode.val
            
            tempNode = tempNode.next
            if (tempNode == None):
                break
            tmp = res
            res = ListNode(next = tmp)

        
        return res
