class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tCount = {}
        sCount = {}

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)

        have = 0
        need = len(tCount)
        l = 0
        res = [-1, -1]
        resLen = float("inf")

        for r in range(len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)

            if s[r] in tCount and sCount[s[r]] == tCount[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        

        return s[res[0]:res[1] + 1]