class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        count = 0
        left = ""
        right = ""

        for i in range(n):
            left += text[i]
            right = text[n-i-1] + right

            if left == right:
                count += 1
                left = ""
                right = ""

        return count