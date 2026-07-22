class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []
        count = {}

        for i, c in enumerate(s):
            if count.get(c, 0) <= i:
                count[c] = i
        
        end = 0
        size = 0
        l = 0
        for r, c in enumerate(s):
            end = max(count.get(c), end)

            if r == end:
                res.append(r - l + 1)
                l = r + 1
            

        return res

