from collections import Counter

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        smallest = min(nums)
        num_count = Counter(nums)
        deletions = 0

        for num in numsDivide:
            if num % smallest != 0:
                return -1

            while num % smallest == 0:
                num //= smallest

        for num in num_count:
            if num != smallest and num_count[num] > 0:
                deletions += num_count[num]

        return deletions
