class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        operations = target[0]

        for i in range(1, len(target)):
            operations += max(target[i] - target[i-1], 0)

        return operations
