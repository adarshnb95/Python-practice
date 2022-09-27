class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squarelist = []
        if nums == None:
            return None
        
        # moving a pointer to seperation of positive and negative numbers
        for i in range(len(nums)):
            if nums[i] >= 0:
                break
        
        # Only positive case
        if i-1 < 0:
            for j in range(len(nums)):
                squarelist.append(nums[j]*nums[j])
            return squarelist

        # Only negative case
        if i >= len(nums)-1 and nums[-1] < 0:
            for j in range(len(nums)-1, -1, -1):
                squarelist.append(nums[j]*nums[j])
            return squarelist
        
        # Mix case
        else:
            j = i
            while j < len(nums) and i > -1:
                if nums[j] > -nums[i]:
                    squarelist.append(nums[i]*nums[i])
                    i -= 1
                else:
                    squarelist.append(nums[j]*nums[j])
                    j += 1
                
                if i < 0 and j <len(nums):
                    squarelist.append(nums[j]*nums[j])
                    j+=1
                elif i > -1 and j == len(nums):
                    squarelist.append(nums[i]*nums[i])
                    i+=1
            return squarelist

if __name__ == "__main__":
    S = Solution()
    print(S.sortedSquares([-1, 1]))