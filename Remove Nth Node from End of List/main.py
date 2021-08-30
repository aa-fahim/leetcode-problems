# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
  Time Complexity: O(n) where n is the number of nodes in the linked list.
  
  Solution uses two pointer solution. One pointer is fast and other pointer is slow. Fast pointer will start at Nth position of the linked list while slow pointer
  will start at the beginning of the linked list. Increment both pointers by 1 until the fast pointer reaches the end of the linked list. At this pointer, we know
  the next node of the slow pointer is the Nth node from end of list. We want to skip this next node and change the connection of the slow pointer node to point at
  the node two positiosn away thus skipping the Nth node from end of list.

'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        
        slow = fast = dummy
        
        print(slow, fast)
        for i in range(n):
            fast = fast.next
            
        while(True):
            if (fast.next == None):
                break
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy.next

        
