class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        res = [0] * len(arr)
        res[len(arr) - 1] = -1
        maxNum = -1

        for i in range(len(res) - 2, -1, -1):
            maxNum = max(arr[i + 1], maxNum)
            res[i] = maxNum

        return res