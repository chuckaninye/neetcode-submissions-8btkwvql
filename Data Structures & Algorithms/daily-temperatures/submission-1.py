class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackInd = stack[-1][0], stack[-1][1]
                res[stackInd] = i - stackInd
                stack.pop()

            stack.append((t, i))

        return res
