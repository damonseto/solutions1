class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memoi = {}

        def dfs(left):
            if left == 0:
                return 0
            if left in memoi:
                return memoi[left]
            mins = 1e9
            for coin in coins:
                if left - coin >= 0:
                    mins = min(mins, 1 + dfs(left - coin))
            memoi[left] = mins
            return mins
        temp = dfs(amount)
        if temp == 1e9:
            return -1
        return temp


        