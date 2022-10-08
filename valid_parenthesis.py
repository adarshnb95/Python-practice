class Solution:
    def isValid(self, s: str) -> bool:
        ref = {"]":"[", "}":"{", ")":"("}
        
        mystack = []
        
        for char in s:
            if char in ref:
                top_element = mystack.pop() if mystack else '#'
                if ref[char] != top_element:
                    return False
            else:
                mystack.append(char)
        
        return not mystack
                
if __name__ == "__main__":
    S = Solution()
    print(S.isValid("[}{{}{]{()("))