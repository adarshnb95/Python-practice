class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def getRange(mid, arr):
            i = mid
            if nums[i+1] == nums[i]:
                j = i
            elif nums[i-1] == nums[i]:
                i = i-1
                j = i
            flag = 0
            while flag < 2:
                if nums[i-1] < nums[i]:
                    flag += 1
                else:
                    i -= 1
                if nums[j+1] > nums[j]:
                    flag += 1
                else:
                    j += 1
            return i, j
        
        if nums == []:
            return [-1, -1]
        if len(nums) == 1:
            if target in nums:
                return [0, 0]
            else:
                return [-1, -1]
        
        start = 0
        end = len(nums) - 1
        i = j = 0
        mid = (start+end)//2
        while start < end and mid != 0 and mid != len(nums):
            mid = (start+end)//2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] == target:
                print("Target found")
                i, j = getRange(mid, nums)
                return [i, j]
                
        return [-1, -1]

if __name__ == "__main__":
    S = Solution()
    print(S.searchRange([2, 2], 3))
