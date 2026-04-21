class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxLength = 0
        consecutive = 0

        for n in nums:
            if n == 1:
                consecutive += 1
            else:
                consecutive = 0
            
            maxLength = max(maxLength, consecutive)

        return maxLength