class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        res = 0
        prefix_sum = 0
        
        for i in range(n-1, -1, -1):
            prefix_sum += satisfaction[i]
            res += prefix_sum
        
        return res if res > 0 else 0
