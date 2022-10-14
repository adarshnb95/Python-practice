class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) == 1:
            return 1
        ref = chars[0]
        count = 0
        ptr = 0
        for char in chars:
            if char == ref:
                if count == 0:
                    count += 1      
                    chars[ptr] = ref
                    ptr += 1
                else:
                    count += 1
                    chars[ptr] = str(count)
            else:
                if count == 1:
                    pass
                else:
                    ref = char
                    count = 1
                    ptr += 1
                    chars[ptr] = ref
                    
        print(chars)
        return len(chars)

if __name__ == "__main__":
    S = Solution()
    print(S.compress(["a", "a", "b", "b", "c", "c", "c"]))