class Solution:
    def rob(self, nums: List[int]) -> int:
        memoiz = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if memoiz[i] != -1:
                return memoiz[i]
            return max(dfs(i+1), nums[i] + dfs(i + 2))
        return dfs(0)

        