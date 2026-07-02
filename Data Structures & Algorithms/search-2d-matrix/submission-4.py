class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        matrixL = 0
        matrixR = len(matrix) - 1
        row = 0

        while matrixL <= matrixR:
            mid = (matrixR + matrixL) // 2

            if matrix[mid][0] > target and matrix[mid][-1] > target:
                matrixR = mid - 1
            elif matrix[mid][0] < target and matrix[mid][-1] < target:
                matrixL = mid + 1
            else:
                row = mid
                break
        
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            m = (r + l) // 2

            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        
        return False

