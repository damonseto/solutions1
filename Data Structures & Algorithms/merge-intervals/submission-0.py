class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def getStart(inta):
            return inta[0]
        n = len(intervals)
        intervals.sort(key = getStart)
        i = 1
        res = []
        res.append(intervals[0])
        b = 1
        while i < n:
            res.append(intervals[i])
            if res[b][0] <= res[b-1][1]:
                res[b-1][1] = res[b][1]
                res.pop()
                b -= 1
            i += 1
            b += 1
        return res
        