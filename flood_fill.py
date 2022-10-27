class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        row, col = len(image), len(image[0])
        curr_color = image[sr][sc]
        if curr_color == color:
            return image
        
        def dfs(r, c):
            if image[r][c] == curr_color:
                image[r][c] = color
                if r >= 1: dfs(r-1, c)
                if r+1 < row: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < col: dfs(r, c+1)
            else:
                return
        
        dfs(sr, sc)
        return image

if __name__ == "__main__":
    S = Solution()
    print(S.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))