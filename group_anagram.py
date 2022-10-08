class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        bigDict = {}
        
        def sortThis(word):
            return "".join(sorted(word))
        
        for word in strs:
            if sortThis(word) in bigDict:
                bigDict[sortThis(word)].append(word)
            else:
                bigDict[sortThis(word)] = [word]
        
        
        final = []
        for items in bigDict.values():
            final.append(items)
        
        return final



if __name__ == "__main__":
    S = Solution()
    print(S.groupAnagrams(["bat","ate","eat","tab","tea","cat"]))