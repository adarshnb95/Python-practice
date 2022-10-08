class Solution:
    def romanToInt(self, s: str) -> int:
        ref = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        i = 0
        result = 0
        while i < len(s)-1:
            if s[i] in ref:
                result+=ref[s[i]]
            if ref[s[i]] < ref[s[i+1]]:
                result -= 2*ref[s[i]]
            i+=1
        result = result+ref[s[i]]
                
        return int(result)

if __name__ == "__main__":
    S = Solution()
    print(S.romanToInt("MCLXXIV"))