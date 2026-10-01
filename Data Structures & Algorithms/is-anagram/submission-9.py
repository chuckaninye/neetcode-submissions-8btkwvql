class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        sCount = [0] * 26
        tCount = [0] * 26

        for c in s:
            sCount[ord(c) - ord('a')] += 1
        
        for c in t:
            tCount[ord(c) - ord('a')] += 1

        for i in range(len(sCount)):
            if sCount[i] != tCount[i]:
                return False
        
        return True