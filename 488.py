from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        count = Counter(hand)
        result = self.backtrack(board, count)
        return result if result != float('inf') else -1

    def backtrack(self, board, count):
        if not board:
            return 0

        res = float('inf')
        i = 0

        while i < len(board):
            j = i
            while j < len(board) and board[j] == board[i]:
                j += 1

            need = 3 - (j - i)
            if count[board[i]] >= need:
                removed = need if need > 0 else 0
                count[board[i]] -= need
                new_board = self.removeConsecutive(board[:i] + board[j:])
                res = min(res, removed + self.backtrack(new_board, count))
                count[board[i]] += need

            i = j

        return res

    def removeConsecutive(self, board):
        i = 0
        while i < len(board):
            j = i
            while j < len(board) and board[j] == board[i]:
                j += 1

            if j - i >= 3:
                return self.removeConsecutive(board[:i] + board[j:])
            else:
                i = j

        return board
