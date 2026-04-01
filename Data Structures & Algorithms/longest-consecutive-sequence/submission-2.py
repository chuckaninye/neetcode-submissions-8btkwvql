class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nSet = set(nums)
        maxLength = 0

        for n in nums:
            length = 1
            while n + 1 in nSet:
                length += 1
                n += 1
            
            maxLength = max(maxLength, length)

        return maxLength