class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        strlen = len(s) -1
        i, j = 0, strlen
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        print(s)
        return None

if __name__ == "__main__":
    S = Solution()
    S.reverseString(["H","E","L","L", "O"])