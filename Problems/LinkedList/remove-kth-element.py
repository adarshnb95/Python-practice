# Delete every kth node from a circular linked list until only one node is left. Also, print the intermediate lists.
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

import unittest

from Shared.Node import Node


class Solution:
    def remove_kth_element(self, root:Node, k: int)-> int:
        pass

class TestMethods(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.solution = Solution()


    def test_empty(self):
        head = Node(1, Node(2, Node(3, Node(4, None))))
        head.next.next.next = head
        self.assertEqual(self.solution.remove_kth_element(head, 2), 2)
        pass

if __name__ == '__main__':
    sol = Solution()
    unittest.main()