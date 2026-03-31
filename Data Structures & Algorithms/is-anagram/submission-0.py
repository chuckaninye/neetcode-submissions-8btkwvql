class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sCount, tCount = {}, {}

        for sChar in s:
            sCount[sChar] = 1 + sCount.get(sChar, 0)

        for tChar in t:
            tCount[tChar] = 1 + tCount.get(tChar, 0)

        for char in s:
            if sCount[char] != tCount.get(char, 0):
                return False
        
        return True