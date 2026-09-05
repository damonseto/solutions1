class Solution:
    def climbStairs(self, n: int) -> int:
        memoiz = [-1] * n
        def dfs(x):
            if x >= n:
                if x == n:
                    return 1
                return 0
            if memoiz[x] != -1:
                return memoiz[x]
            memoiz[x] = dfs(x + 1) + dfs(x + 2)
            return memoiz[x]
        return dfs(0)
        