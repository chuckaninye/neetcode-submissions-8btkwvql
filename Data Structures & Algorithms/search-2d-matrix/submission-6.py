class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bot = len(matrix) - 1
        row = 0

        while top <= bot:
            mid = (top + bot + 1) // 2

            if matrix[mid][0] < target and matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target and matrix[mid][-1] > target:
                bot = mid - 1
            else:
                row = mid
                break
        
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            mid = (l + r + 1) // 2

            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        
        return False