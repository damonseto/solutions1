class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [-1] * len(nums)
        mem2 = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if mem[i] != -1:
                return mem[i]
            mem[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return mem[i]
        def dfs2(i):
            if i >= len(nums)-1:
                return 0
            if mem2[i] != -1:
                return mem2[i]
            mem2[i] = max(dfs2(i+1), nums[i] + dfs2(i+2))
            return mem2[i]
        return max(dfs2(0), dfs(1))