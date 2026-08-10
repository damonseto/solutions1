class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = stones 
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)
            if x == y:
                pass
            else:
                heapq.heappush(stones, -1 * abs(x-y))
        if len(stones) == 0:
            return 0
        return -1*stones[0]
        