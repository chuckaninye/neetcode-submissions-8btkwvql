class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = []
        dp.append(nums[0])

        for i in range(1, len(nums)):
            sum = nums[i] + dp[-1]

            if nums[i] > sum:
                dp.append(nums[i])
            else:
                dp.append(sum)

        return max(dp)