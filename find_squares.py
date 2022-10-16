class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        if num == 1:
            return True
        end = num
        while start < end:
            mid = start + (end-start)//2
            if mid*mid > num:
                end = mid
            elif mid*mid < num:
                start = mid+1
            elif mid*mid == num:
                return True
        return False

if __name__ == "__main__":
    S = Solution()
    print(S.isPerfectSquare(7437))