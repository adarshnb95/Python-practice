class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        countdict = {}
        for letter in s:
            if letter in countdict:
                countdict[letter] += 1
            else:
                countdict[letter] = 1
        
        
        s = sorted(countdict, key = lambda x: countdict[x], reverse = True)
        
        for letter in s:
            result += letter * countdict[letter]
            
        return result

if __name__ == "__main__":
    S = Solution()
    print(S.frequencySort("tree"))