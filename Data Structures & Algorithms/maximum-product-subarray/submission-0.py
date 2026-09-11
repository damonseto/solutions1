class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        final = max(nums)
        lmax = 1
        lmin = 1
        for n in nums:
            if n == 0:
                lmax, lmin = 0, 0
                continue
            temp = lmax * n
            lmax = max(temp, lmin * n, n)
            lmin = min(temp, lmin * n, n)
            if final < max(lmax, lmin):
                final = max(lmax, lmin)
        return final


        