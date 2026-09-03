class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = []
        board = [-1] * n
        def is_safe(row, col):
            for i in range(row):
                if board[i] == col or abs(board[i] - col) == abs(i - row):
                    return False
            return True
        def backtrack(row):
            if row == n:
                formatted_solution = []
                for i in range(n):
                    line = ["."] * n
                    line[board[i]] = "Q"
                    formatted_solution.append("".join(line))
                solutions.append(formatted_solution)
                return
            for col in range(n):
                if is_safe(row, col):
                    board[row] = col
                    backtrack(row + 1)
                    board[row] = -1
        backtrack(0)
        return solutions
        