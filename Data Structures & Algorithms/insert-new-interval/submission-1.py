class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        start, end = newInterval
        i = 0

        while i < len(intervals) and start > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        while i < len(intervals) and end >= intervals[i][0]:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        
        res.append([start, end])

        while i < len(intervals):
            res.append(intervals[i])
            i += 1


        return res