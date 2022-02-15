from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if prevEnd <= start:
                prevEnd = end
            else:
                prevEnd = min(prevEnd, end)
                res += 1

        return res


intervals = [[1,2],[2,3],[3,4],[1,3]]
print(Solution().eraseOverlapIntervals(intervals))
