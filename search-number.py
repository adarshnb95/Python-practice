# Given a sorted array of distinct integers and a target value, return the index if the target is found.
#  If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchIndex(self, nums, target: int) -> int:
        

s = Solution()
print(s.searchIndex([1,2,3,4,5], 4))
print(s.searchIndex([2,4,6,8,10], 6))
print(s.searchIndex([1,4,7,10,13,16,19], 11))
