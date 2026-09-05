class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(x):
            if x >= n:
                if x == n:
                    return 1
                return 0
            return dfs(x + 1) + dfs(x + 2)
        return dfs(0)
        