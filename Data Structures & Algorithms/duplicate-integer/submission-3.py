class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nSet = set()

        for i, n in enumerate(nums):
            if n in nSet:
                return True
            
            nSet.add(n)

        return False