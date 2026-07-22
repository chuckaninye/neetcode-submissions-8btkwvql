class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nMap = {}

        for i, n in enumerate(nums):
            complement = target - n

            if complement in nMap:
                return [nMap.get(complement), i]
            
            nMap[n] = i

        return []