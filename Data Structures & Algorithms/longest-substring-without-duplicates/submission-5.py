class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        cSet = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1
            
            maxLength = max(maxLength, r - l + 1)
            cSet.add(s[r])
        
        return maxLength