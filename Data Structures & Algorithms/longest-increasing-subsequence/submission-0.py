class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        leng = len(nums)
        memo = [1] * leng

        for i in range(leng - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j])
        return max(memo)


        