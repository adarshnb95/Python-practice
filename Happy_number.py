class Solution:
    def isHappy(self, n: int) -> bool:
        def splitDigits(val) -> list():
            templist = list()
            while val > 0:
                if val > 10:
                    templist.append(val%10)
                elif val < 10:
                    templist.append(val)                    
                val = val//10
            return templist
        
        def sumOfSquaresList(templist: list()) -> int:
            sumsquare = 0
            for i in range(len(templist)):
                sumsquare = sumsquare + (templist[i]*templist[i])
            return sumsquare
        
        result = n
        ResultSet = set()
        while result not in ResultSet and result != 1:
            ResultSet.add(result)
            templist = splitDigits(result)
            result = sumOfSquaresList(templist)
        
        if result == 1:
            return True
        else:
            return False

if __name__ == "__main__":
    S = Solution()
    print(S.isHappy(45))