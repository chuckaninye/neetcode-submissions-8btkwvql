class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        bottle = 0

        for p, s in sorted(zip(position, speed), reverse = True):
            eta = (target - p) / s
            if eta > bottle:
                bottle = eta
                res += 1
        
        return res