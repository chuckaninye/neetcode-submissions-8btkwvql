class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)
        l = r = 0

        for i in range(len(height)):
            maxL[i] = l
            l = max(l, height[i])
        
        for i in range(len(height) - 1, -1, -1):
            maxR[i] = r
            r = max(r, height[i])

        res = 0
        for i in range(len(height)):
            minHeight = min(maxR[i], maxL[i])
            res += max(0, minHeight - height[i])
        
        return res