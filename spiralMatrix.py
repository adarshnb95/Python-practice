class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        outputmtx = []
        
        # We have 4 motions in the spiral, we will divide accordingly.
        
        while matrix is not [[]]:
            #First motion - right
            for i in range(len(matrix[0])):
                outputmtx.append(matrix[0][i])
            matrix.pop(0)
            #Check for break
            if matrix == []:
                return outputmtx

            #Second motion - down
            for i in range(len(matrix)):
                outputmtx.append(matrix[i].pop(-1))
            #Check for break
            print(len(matrix))
            if not matrix:
                return outputmtx

            #Third motion - left
            for i in range(len(matrix[0])-1, -1, -1):
                outputmtx.append(matrix[-1][i])
            matrix.pop(-1)
            #Check for break
            if not matrix:
                return outputmtx

            #Fourth motion - up
            for i in range(len(matrix), 0):
                outputmtx.append(matrix[i].pop(0))
            #Check for break
            if not matrix:
                return outputmtx


if __name__ == "__main__":
    S = Solution()
    print(S.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))
