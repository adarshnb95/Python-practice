# Delete every kth node from a circular linked list until only one node is left.
# Examples:  

# Input : n=4, k=2, list = 1->2->3->4
# Output : 
# 1->2->3->4->1
# 1->2->4->1
# 2->4->2
# 2->2

# Input : n=9, k=4, list = 1->2->3->4->5->6->7->8->9
# Output :
# 1->2->3->4->5->6->7->8->9->1
# 1->2->3->4->6->7->8->9->1
# 1->2->3->4->6->7->8->1
# 1->2->3->6->7->8->1
# 2->3->6->7->8->2
# 2->3->6->8->2
# 2->3->8->2
# 2->3->2
# 2->2

# counter = 0
# itr = root
# if itr = Null then return null?
# while true:
#       if itr.next = itr then break
#       if counter == k-1 then itr.next= itr.next.next and counter = 0
#       counter +=1
#       itr = itr.next
# return itr.data
# 
# while true:
#   if itr.next == root then itr.next = itr
#       break




import unittest

from Shared.Node import Node


class Solution:
    def remove_kth_element(self, root:Node, k: int)-> int:      # root = 1->2->3->4->1      k = 2
        counter = 0         
        itr = root          
        if itr == None:         
            return None

        if k == 0:
            while True:
                if itr.next == root:
                    itr.next = itr
                    break
                itr = itr.next
        else:
            while True:     # 
                if itr.next == itr:   # false ;false; false
                    break
                if counter == k-1:      # false; true; false
                    itr.next = itr.next.next        # ;4
                    counter = 0                     # ;0
                counter += 1        # 1; 1; 2
                itr = itr.next      # 2; 4;
        return itr.data


    # def printLL(self, root):


class TestMethods(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_empty(self):
        head = None
        self.assertEqual(self.solution.remove_kth_element(head, 10), None) #answer should be none

    def test_not_empty(self):
        head = Node(1, Node(2, Node(3, Node(4, None))))
        head.next.next.next.next = head
        self.assertEqual(self.solution.remove_kth_element(head, 2), 2)

        head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, None)))))))))
        head.next.next.next.next.next.next.next.next.next = head
        self.assertEqual(self.solution.remove_kth_element(head, 4), 2)

        head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, None)))))))))
        head.next.next.next.next.next.next.next.next.next = head
        self.assertEqual(self.solution.remove_kth_element(head, 0), 9)

if __name__ == '__main__':
    unittest.main()