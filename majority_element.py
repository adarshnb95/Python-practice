class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

if __name__ == "__main__":
    S = Solution()
    print(S.majorityElement([2, 5, 6, 3, 3, 3, 3, 3, 2, 5, 7]))