class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        total = 0
        if n == 0:
            return total
        adj = []
        for i in range(n):
            adj.append([])
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        been = set()

        def dfs(node):
            if node in been:
                return
            been.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        for i in range(n):
            if i not in been:
                total += 1
                dfs(i)
        return total
        