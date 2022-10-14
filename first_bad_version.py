class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while end > start:
            mid = start + (end-start)/2
            if self.isBadVersion(mid):
                end = mid
            else:
                start = mid+1
                
        return int(start)

    def isBadVersion(self, num:int) -> bool:
        if num >= 4:
            return True
        else:
            return False

if __name__ == "__main__":
    S = Solution()
    print(S.firstBadVersion(7))