# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
  Time Complexity: O(n * logn) where n is the number of nodes in the linked list. We find the middle of the linked list which takes logn time then create a TreeNode 
  for every node in the linked list which takes n time.
  
'''
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return
        elif not head.next:
            return TreeNode(head.val)

        slow, fast, prev = head, head, None
        
        while(fast != None and fast.next != None):
            fast = fast.next.next
            prev = slow
            slow = slow.next

        node = TreeNode(slow.val)
        prev.next = None
        
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        
        return node
