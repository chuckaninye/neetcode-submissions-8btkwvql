class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1
        
        pre = len(nums) - 2
        suf = len(nums) - 1

        while pre >= 0:
            if nums[pre] == nums[suf]:
                del nums[pre]
            
            pre -= 1
            suf -= 1
        
        return len(nums)