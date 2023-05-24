class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def mergeSortCount(lo, hi):
            if lo == hi:
                return 0

            mid = lo + (hi - lo) // 2
            count = mergeSortCount(lo, mid) + mergeSortCount(mid + 1, hi)

            i = j = mid + 1
            for left in prefixSums[lo:mid + 1]:
                while i <= hi and prefixSums[i] - left < lower:
                    i += 1
                while j <= hi and prefixSums[j] - left <= upper:
                    j += 1
                count += j - i

            prefixSums[lo:hi + 1] = sorted(prefixSums[lo:hi + 1])

            return count

        prefixSums = [0]
        for num in nums:
            prefixSums.append(prefixSums[-1] + num)

        return mergeSortCount(0, len(prefixSums) - 1)
