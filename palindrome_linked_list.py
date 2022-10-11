# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        flag = 0
        first = []
        
        if head == None:
            return False
        elif head.next == None:
            return True
        
        while fast:
            fast = fast.next
            if flag == 1:
                first.append(slow.val)
                slow = slow.next
            flag = 1 - flag
        
        # if length is odd:
        if flag == 1 and slow.next:    
            slow = slow.next
        
        # Common after odd length check
        while slow and first != []:
            if first[-1] != slow.val:
                return False
            else:
                slow = slow.next
                first.pop()
        
        if slow == None and first == []:
            return True
        else:
            return False