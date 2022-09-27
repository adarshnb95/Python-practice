class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        zeropointer = 0
        # First zero check
        while nums[zeropointer] != 0:
            zeropointer+=1
            if zeropointer+1 >= len(nums):
                return None
        
        # Now we have a current pointer traversing through nums, and we see non zero item, we swap it with zeropointer, and increment zeropointer
        
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[zeropointer], nums[curr] = nums[curr], nums[zeropointer]
                zeropointer += 1
        
        print(nums)
        
        return None

if __name__ == "__main__":
    S = Solution()
    print(S.moveZeroes([1, 0, 0, 2, 4, 0, 0, 4, 0, 7]))