class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31-1
        visit = set()
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                ro, co = r + dr, c + dc
                if (ro >= 0 and co >= 0 and ro < len(grid) and co < len(grid[0]) and 
                grid[ro][co] == INF):
                    grid[ro][co] = grid[r][c] + 1
                    q.append((ro,co))
