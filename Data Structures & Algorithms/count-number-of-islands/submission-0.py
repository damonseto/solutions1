class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row, col = q.popleft()
                directions = [[-1,0],[1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    ro, co = dr + row, dc + col
                    if (ro in range(len(grid)) and co in range(len(grid[0]))
                    and grid[ro][co] == "1" and (ro,co) not in visited):
                        visited.add((ro, co))
                        q.append((ro, co))
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands
            
        