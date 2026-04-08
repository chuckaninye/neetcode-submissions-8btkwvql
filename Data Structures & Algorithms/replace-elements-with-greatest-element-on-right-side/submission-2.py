class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        res = [0] * len(arr)
        maxNum = -1

        for i in range(len(res) - 1, -1, -1):
            res[i] = maxNum
            maxNum = max(arr[i], maxNum)

        return res