class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest_sum):
            subarray_count = 0
            current_sum = 0

            for num in nums:
                current_sum += num
                if current_sum > largest_sum:
                    subarray_count += 1
                    current_sum = num

            # After the loop, we might have some remaining sum
            if current_sum > 0:
                subarray_count += 1

            return subarray_count <= k

        # Binary search for the minimum largest sum
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = left + (right - left) // 2

            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left
