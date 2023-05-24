from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        n = len(points)
        deque_points = deque()
        max_value = float('-inf')

        for j in range(n):
            xj, yj = points[j]

            while deque_points and xj - points[deque_points[0]][0] > k:
                deque_points.popleft()

            if deque_points:
                xi, yi = points[deque_points[0]]
                max_value = max(max_value, yi + yj + (xj - xi))

            while deque_points and yj - xj >= points[deque_points[-1]][1] - points[deque_points[-1]][0]:
                deque_points.pop()

            deque_points.append(j)

        return max_value
