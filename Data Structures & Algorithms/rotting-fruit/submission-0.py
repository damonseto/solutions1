class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        shortest = -1
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        while q:
            r, c = q.popleft()
            for dr, dc in dir:
                if 0<=r + dr<len(grid) and 0<=c + dc<len(grid[0]) and grid[r + dr][c + dc] == 1:
                    grid[r + dr][c + dc] = grid[r][c] + 1
                    q.append((r + dr, c + dc))
        highest = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
                if grid[r][c] > highest:
                    highest = grid[r][c]
        return highest - 2
                    


        