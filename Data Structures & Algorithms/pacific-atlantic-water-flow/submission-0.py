class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        direc = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs1(r, c, prev):
            if (r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]) or 
            (r, c) in pacific or heights[r][c] < prev):
                return
            pacific.add((r, c))
            for dr, dc in direc:
                dfs1(r + dr, c + dc, heights[r][c])
        def dfs2(r, c, prev):
            if (r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]) or
            (r, c) in atlantic or heights[r][c] < prev):
                return
            atlantic.add((r, c))
            for dr, dc in direc:
                dfs2(r + dr, c + dc, heights[r][c])


        for i in range(len(heights)):
            dfs1(i, 0, 0)
        for i in range(len(heights[0]) - 1):
            dfs1(0, i + 1, 0)
        for i in range(len(heights)):
            dfs2(i, len(heights[0])-1, 0)
        for i in range(len(heights[0]) - 1):
            dfs2(len(heights)-1, i + 1, 0)

        return list(pacific & atlantic)
        