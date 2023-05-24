class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        stack = []
        result = [-1] * n

        for i in range(n - 1, -1, -1):
            position, speed = cars[i]

            while stack:
                j = stack[-1]
                prev_position, prev_speed = cars[j]

                if speed <= prev_speed or \
                        (position - prev_position) / (speed - prev_speed) >= result[j] > 0:
                    stack.pop()
                else:
                    break

            if stack:
                j = stack[-1]
                prev_position, prev_speed = cars[j]
                result[i] = (prev_position - position) / (speed - prev_speed)

            stack.append(i)

        return result
