class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelset = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        voweldict = []
        for letter in s:
            if letter in vowelset:
                voweldict.append(letter)
        
        res = []
        
        for letter in s:
            if letter in vowelset:
                res.append(voweldict.pop())
            else:
                res.append(letter)
        
        return "".join(res)

if __name__ == "__main__":
    S = Solution()
    print(S.reverseVowels(["H","E","L","L", "O"]))