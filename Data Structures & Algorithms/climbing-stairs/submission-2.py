class Solution:
    def climbStairs(self, n: int) -> int:
        
        #0 1 2
        #    ^  (one)
        #  ^    (one)
        #^      (two)
        #0  1   2   3   4   5
        #                   ^  (one)
        #               ^      (one)
        #           ^          (two)
        #       ^              (three)

        one = 1
        two = 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one