class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        avg = s / n

        # if there is only one element, we cannot split the array
        if n == 1:
            return False

        # check if any one element equals to the average
        if avg in nums:
            return True

        # sort the array in decreasing order to try larger elements first
        nums.sort(reverse=True)

        # try all possible sizes for array A
        for size_a in range(1, n // 2 + 1):
            # if the sum of size_a elements is not divisible by size_a, skip
            if (s * size_a) % n != 0:
                continue
            sum_a = avg * size_a
            # if we can make array A with sum sum_a, we are done
            if self.can_make_sum(nums, sum_a, size_a):
                return True
        return False

    # check if we can make sum with exactly k elements
    def can_make_sum(self, nums, sum, k):
        if k == 0:
            return sum == 0
        if sum < 0 or k > len(nums):
            return False
        return self.can_make_sum(nums[1:], sum - nums[0], k - 1) or self.can_make_sum(nums[1:], sum, k)
