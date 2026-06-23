class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = mid = 0
        right = len(nums) - 1

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while mid <= right:
            if nums[mid] == 0:
                swap(mid, left)
                left += 1
                mid += 1
            elif nums[mid] == 2:
                swap(mid, right)
                right -= 1
            else:
                mid += 1