class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        
        # Calculate the cost of changing s[i:j+1] to a palindrome.
        # This will be used to fill in the dp table.
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                cost[i][j] = cost[i+1][j-1] + (s[i] != s[j])
        
        # Initialize the dp table.
        # dp[i][j] is the minimal cost to divide s[0:i+1] into j+1 palindromes.
        dp = [[float('inf')] * k for _ in range(n)]
        for i in range(n):
            dp[i][0] = cost[0][i]
        
        # Fill in the dp table using bottom-up dynamic programming.
        for i in range(1, n):
            for j in range(1, k):
                for x in range(j-1, i):
                    dp[i][j] = min(dp[i][j], dp[x][j-1] + cost[x+1][i])
        
        return dp[n-1][k-1]
