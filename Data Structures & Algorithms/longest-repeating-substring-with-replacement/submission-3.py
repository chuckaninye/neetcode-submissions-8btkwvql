class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        maxFreq = 0
        count = {}
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])

            if r - l + 1 - maxFreq <= k:
                res = max(res, r - l + 1)

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
        
        return res