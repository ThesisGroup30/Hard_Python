class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        n = len(locations)
        dp = [[0] * n for _ in range(fuel + 1)]
        dp[fuel][start] = 1
        
        for f in range(fuel, -1, -1):
            for i in range(n):
                for j in range(n):
                    if i != j:
                        dist = abs(locations[i] - locations[j])
                        if f >= dist:
                            dp[f-dist][j] += dp[f][i]
                            dp[f-dist][j] %= MOD
        
        return sum(dp[i][finish] for i in range(fuel+1)) % MOD
