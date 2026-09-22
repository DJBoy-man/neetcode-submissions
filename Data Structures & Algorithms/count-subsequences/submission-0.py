class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        rows = len(s)
        cols = len(t)

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Empty t can be formed in 1 way

        for i in range(rows + 1):
            dp[i][cols] = 1
        
        for i in range(rows - 1, -1, -1):
            for j in range(cols -1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        
        return dp[0][0]
      
        
