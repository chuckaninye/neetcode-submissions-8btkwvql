class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        countR = {}
        countM = {}

        for c in ransomNote:
            countR[c] = 1 + countR.get(c, 0)
        
        for c in magazine:
            countM[c] = 1 + countM.get(c, 0)

        for c in ransomNote:
            if countM.get(c, 0) < countR[c]:
                return False

        return True