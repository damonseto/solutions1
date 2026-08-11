class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = []
        counts = Counter(tasks)
        for cnt in counts.values():
            maxheap.append(-cnt)
        heapq.heapify(maxheap)
        q = deque() # [left, time until workable]
        time = 0
        while maxheap or q:
            time += 1
            if maxheap:
                temp = heapq.heappop(maxheap) + 1
                if temp != 0:
                    q.append([temp, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time
