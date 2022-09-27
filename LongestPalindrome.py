class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def checkPalindrome(checkstring:str):
            i = 0
            j = len(checkstring) - 1

            while i < j:
                if checkstring[i] != checkstring[j]:
                    return False
                i+=1
                j-=1

            return True
        
        if s is None:
            return None
        elif len(s) == 1:
            return s
        
        longest = ""
        
        i = int(len(s)/2)
        j = i+1
        flag = 0
        
        while i >= -1 and j <= len(s):
            if checkPalindrome(s[i:j+1]):
                longest = s[i:j+1]
            
            if flag == 0:
                i -= 1
            elif flag == 1:
                j += 1
            
            flag = 1 - flag
        
        return longest

if __name__ == "__main__":
    S = Solution()
    print(S.longestPalindrome("babad"))