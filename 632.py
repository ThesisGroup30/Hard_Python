from heapq import heappush, heappop

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # heap contains (value, list_index, value_index) tuples
        heap = [(lst[0], i, 0) for i, lst in enumerate(nums)]
        # keep track of the maximum value in the heap
        max_val = max(lst[0] for lst in nums)
        # initialize the smallest range to be from the first element of the first list to the maximum value
        smallest_range = [heap[0][0], max_val]
        while True:
            # pop the smallest element from the heap
            min_val, lst_idx, val_idx = heappop(heap)
            # if the new range is smaller than the current smallest range, update the smallest range
            if max_val - min_val < smallest_range[1] - smallest_range[0]:
                smallest_range = [min_val, max_val]
            # if we have reached the end of the list, we are done
            if val_idx == len(nums[lst_idx]) - 1:
                break
            # add the next element from the same list to the heap
            heappush(heap, (nums[lst_idx][val_idx+1], lst_idx, val_idx+1))
            # update the maximum value if necessary
            max_val = max(max_val, nums[lst_idx][val_idx+1])
        return smallest_range
