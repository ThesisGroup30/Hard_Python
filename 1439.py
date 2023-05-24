import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        heap = [(sum(mat[i][0] for i in range(m))), [0] * m]
        visited = set(tuple([0] * m))

        for _ in range(k - 1):
            curr_sum, indices = heapq.heappop(heap)
            for i in range(m):
                if indices[i] + 1 < n and tuple([indices[j] if j != i else indices[j] + 1 for j in range(m)]) not in visited:
                    new_indices = [indices[j] if j != i else indices[j] + 1 for j in range(m)]
                    heapq.heappush(heap, (curr_sum - mat[i][indices[i]] + mat[i][indices[i] + 1], new_indices))
                    visited.add(tuple(new_indices))

        return heap[0][0]
