class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ans = -1
        count = 0

        for n in nums:
            if count == 0 and ans != n:
                ans = n
            elif ans == n:
                count += 1
            else:
                count -= 1
        
        return ans