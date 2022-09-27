class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        substring = set()
        strlength = 0
        i = 0
        for j in range(i, len(s)):
            if s[j] in substring:
                substring.remove(s[j])
                i+=1
            else:
                strlength = max(strlength, len(substring)+1)
                substring.add(s[j])
        return strlength


if __name__ == "__main__":
    sub = Solution()
    print(f"The length of the longest substring is ", sub.lengthOfLongestSubstring("pwwkew"))
