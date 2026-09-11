class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = set()
        def dfs(cur):
            if cur == s:
                return True
            if len(cur) >= len(s):
                return False
            if cur in mem:
                return False
            left = s[len(cur):]

            for word in wordDict:
                if left[:len(word)] == word:
                    if dfs(cur+word):
                        return True
            mem.add(cur)
            return False
        return dfs("")
       
            
        