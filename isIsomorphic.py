class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictmap = {}
        for index in range(len(s)):
            if s[index] in dictmap:
                if dictmap[s[index]] != t[index]:
                    return False
            else:
                dictmap[s[index]] = t[index]
        
        return True

if __name__ == "__main__":
    S = Solution()
    print(S.isIsomorphic("badc", "baba"))