class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            # If we can freely rearrange the string, just sort it lexicographically
            return ''.join(sorted(s))
        else:
            # If k = 1, we need to consider all possible rotations of the string to find the lexicographically smallest one
            n = len(s)
            smallest_rotation = s
            for i in range(1, n):
                # Rotate the string by i characters
                rotated = s[i:] + s[:i]
                if rotated < smallest_rotation:
                    smallest_rotation = rotated
            return smallest_rotation
