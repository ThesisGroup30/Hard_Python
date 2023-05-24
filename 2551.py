class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            count = 0
            curr_sum = 0
            max_sum = 0

            for i in range(n):
                if curr_sum + weights[i] > mid:
                    count += 1
                    max_sum = max(max_sum, curr_sum)
                    curr_sum = weights[i]
                else:
                    curr_sum += weights[i]

            count += 1
            max_sum = max(max_sum, curr_sum)

            if count <= k:
                right = max_sum
            else:
                left = mid + 1

        return left - max_sum
