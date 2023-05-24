class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        n = len(rolls)
        # dp[i][j] stores the length of the shortest sequence that cannot be taken from rolls[0:i] using a k-sided dice, if the last roll is j
        dp = [[0] * k for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(k):
                # if we can take the current roll, the shortest sequence is the same as the shortest sequence for rolls[0:i-1]
                if rolls[i-1] == j+1:
                    dp[i][j] = dp[i-1][j]
                # otherwise, we need to add the current roll to the end of some shortest sequence for rolls[0:i-1]
                else:
                    dp[i][j] = dp[i-1][j] + 1
                # check if we can construct a sequence of length i using rolls[0:i] with the last roll j
                for l in range(1, i+1):
                    if all((rolls[m] == j+1) or (rolls[m] not in range(1, j+1)) for m in range(i-l, i)):
                        dp[i][j] = min(dp[i][j], l)
        # return the minimum length of any sequence that cannot be taken from rolls
        return min(dp[n])
