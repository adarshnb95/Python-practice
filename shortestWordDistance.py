class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        findDict = {}
        findDict[word1] = -1
        findDict[word2] = -1
        dist = len(wordsDict)
        flag = 0
        for word in wordsDict:
            if word in findDict:
                findDict[word] = wordsDict.index(word)
                flag = 1 if flag == 0 else 0
                if flag == 0:
                    dist = min(dist, abs(findDict[word1] - findDict[word2]))
                    flag = 1
            if flag == 1:
                dist += 1
        return dist
        


if __name__ == "__main__":
    S = Solution()
    print(S.shortestDistance(["a", "new", "place", "for", "me"], "new", "place"))