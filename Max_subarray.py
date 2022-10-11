class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr = maxsum = nums[0]
        for num in nums[1:]:
            curr = max(num, curr+num)
            maxsum = max(maxsum, curr)
            
        return maxsum

if __name__ == "__main__":
    S = Solution()
    print(S.maxSubArray([-2,1,-3,-2,4, 2, -3, 6, 1, -4, 5]))