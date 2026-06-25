class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            target = -1 * nums[i]

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:
                curSum = nums[j] + nums[k]
                if curSum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif curSum > target:
                    k -= 1
                else:
                    j += 1
        return res
