'''
logic:
linkedlist = 0-1-2-3-4-5-6-7-8
nums = 5,3,2,1,6

checkedstack = 0

connected_counter = 1
previously_connected = True

if val in nums and prev_con == False:
    remove from nums
    counter += 1
    prev_con = True
    
if val in nums and prev_con == True:
    remove from nums
else:
    prev_con = False

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: ListNode, nums: list[int]) -> int:
        if head is None or nums is None:
            return 0
        
        itr = head
        connected_counter = 0
        prev_con = False
        
        while itr and nums:
            if itr.val in nums and prev_con == False:
                nums.remove(itr.val)
                connected_counter += 1
                prev_con = True
            elif itr.val in nums and prev_con == True:
                nums.remove(itr.val)
            else:
                prev_con = False
            itr = itr.next
        return connected_counter
    
    