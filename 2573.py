class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [''] * n

        for i in range(n):
            for j in range(i + 1, n):
                common_len = min(lcp[i][j], lcp[j][i])
                for k in range(common_len):
                    word[i] += word[j][k]
                if lcp[i][j] > common_len:
                    word[i] += chr(ord(word[j][common_len]) + 1)
                elif lcp[j][i] > common_len:
                    word[i] += chr(ord(word[i][common_len]) + 1)
                else:
                    word[i] += 'a'

        return word[0]
