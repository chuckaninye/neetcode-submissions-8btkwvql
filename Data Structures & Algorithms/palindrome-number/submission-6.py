class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x == 0:
            return True
        
        if x % 10 == 0:
            return False
        
        reversedX = 0
        while x > reversedX:
            reversedX = reversedX * 10 + (x % 10)
            x = x // 10
        
        return True if x == reversedX or x == reversedX // 10 else False