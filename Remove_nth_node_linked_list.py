# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None
        
        fast, slow = head, head
        
        
        prev = None
        for i in range(n):
            fast = fast.next
            
        if fast is None:
            return head.next
        
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        if slow.next == None:
            prev.next = None
        else:
            prev.next = slow.next
        return head

