from collections import Counter

class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums_counter = Counter(nums)
        target_counter = Counter(target)
        operations = 0

        for num, freq in target_counter.items():
            diff = freq - nums_counter[num]
            if diff > 0:
                operations += diff

        return operations
