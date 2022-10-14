# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         if len(s3) != len(s1) + len(s2):
#             return False
        
#         i, j, k = 0, 0, 0
#         for k in range(len(s3)-2):
#             if s3[k] != s1[i] and s3[k] != s2[j]:
#                 return False
#             elif s3[k] == s1[i] and s1[i]:
#                 i += 1
#             elif s3[k] == s2[j] and s2[j]:
#                 j += 1
        
#         return True

# if __name__ == "__main__":
#     S = Solution()
#     print(S.isInterleave("", "", "a"))