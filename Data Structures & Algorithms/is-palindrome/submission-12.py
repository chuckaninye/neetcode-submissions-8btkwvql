class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1

        def isAlphaNum(c):
            return (ord('a') <= ord(c) and ord(c) <= ord('z')) or (ord('0') <= ord(c) and ord(c) <= ord('9'))

        while l < r:
            while l < r and not isAlphaNum(s[l].lower()):
                l += 1

            while l < r and not isAlphaNum(s[r].lower()):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True