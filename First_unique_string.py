class Solution:
    def firstUniqChar(self, s: str) -> int:
        letterdict = {}
        
        for i, letter in enumerate(s):
            if letter in letterdict:
                letterdict[letter] += 1
            else:
                letterdict[letter] = 1
        
        for i, letter in enumerate(s):
            if letter in letterdict and letterdict[letter] == 1:
                return i
        
        return -1

if __name__ == "__main__":
    S = Solution()
    print(S.firstUniqChar("leetcode"))