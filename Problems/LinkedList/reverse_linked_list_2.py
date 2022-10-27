# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#         itr = head
#         counter = 1
#         tempList = ListNode()
#         while itr:
#             if counter == left:
#                 tempList = ListNode(itr.val)
                
#             elif counter == right:
#                 tempList.next = ListNode(itr.val)
#                 tempList.val
#             elif counter > left and counter < right:
#                 tempList.next = ListNode(itr.val)
            
#             itr = itr.next
            
#     def reverseLinkedList(self, head):
#         prev, curr = None, head

#         while curr:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
#         return prev

class Solution:
    def reverseBetween(self, head:ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0, head)
        
        leftPrev, curr = dummy, head
        for i in range(left - 1):
            leftPrev, curr = curr, curr.next
        
        # Reversing from here
        prev = None
        for i in range(right-left + 1):
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        
        # Assigning links
        leftPrev.next.next = curr
        leftPrev.next = prev
        return dummy.next
            