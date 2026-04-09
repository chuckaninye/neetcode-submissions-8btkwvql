class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        m = len(word)
        n = len(abbr)
        i = 0
        j = 0

        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isalpha() or abbr[j] == "0":
                return False
            else:            
                sublen = 0
                while j < n and not abbr[j].isalpha():
                    sublen = sublen * 10 + int(abbr[j])
                    j += 1
                
                i += sublen
        
        return i == m and j == n

