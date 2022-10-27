class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ListS = list(s)
        i, j = 0, len(s) - 1
        while i< j:
            if ListS[i].isalpha() and ListS[j].isalpha():
                ListS[i], ListS[j] = ListS[j], ListS[i]
                i += 1
                j -= 1
            if not ListS[i].isalpha():
                i += 1
            if not ListS[j].isalpha():
                j -= 1
        return "".join(ListS)

if __name__ == "__main__":
    S = Solution()
    print(S.reverseOnlyLetters("bc-da"))