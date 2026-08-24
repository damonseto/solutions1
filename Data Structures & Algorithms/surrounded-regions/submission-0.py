class Solution:
    def solve(self, board: List[List[str]]) -> None:
        been = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r, c):
            if (len(board) <= r or r < 0 or len(board[0]) <= c or c < 0 or 
            board[r][c] == "X" or (r, c) in been):
                return
            been.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)
        for i in range(len(board[0])-1):
            dfs(0, i + 1)
            dfs(len(board)-1, i + 1)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r,c) not in been and board[r][c] == "O":
                    board[r][c] = "X"