class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        
        def flip(row:list):
            return row[::-1]
        
        def invert(row:list):
            for i in row:
                if i == 1:
                    i = 0
                elif i == 0:
                    i = 1
            
            return row
        
        ans = []
        for row in image:
            ansrow = flip(row)
            ansrow = invert(ansrow)
            ans.append(ansrow)
        
        return ans

if __name__ == "__main__":
    S = Solution()
    S.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])