class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ksmallest = []
        for i in range(len(points)):
            dist = math.sqrt((points[i][0])**2 + (points[i][1])**2)
            heapq.heappush(ksmallest, (-dist, points[i]))
            if len(ksmallest) > k:
                heapq.heappop(ksmallest)
        res = []
        for i in range(len(ksmallest)):
            res.append(ksmallest[i][1])
        return res

        