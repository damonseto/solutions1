"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        trans = {}
        if not node:
            return None
        def dfs(node):
            if node in trans:
                return trans[node]
            copy = Node(node.val)
            trans[node] = copy
            for neib in node.neighbors:
                copy.neighbors.append(dfs(neib))
            return copy
        
        return dfs(node)
        