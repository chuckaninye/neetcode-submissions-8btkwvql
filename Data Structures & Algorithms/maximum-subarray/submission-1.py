class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        greedy = [float("-inf")] * len(nums)
        greedy[0] = nums[0]

        for i in range(1, len(nums)):
            greedy[i] = max(nums[i], greedy[i - 1] + nums[i])

        return max(greedy)