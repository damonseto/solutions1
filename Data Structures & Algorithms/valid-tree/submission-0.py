class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = []
        for i in range(n):
            adj.append([])
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        been = set()

        def dfs(node, par):
            if node in been:
                return False
            been.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(been) == n
        