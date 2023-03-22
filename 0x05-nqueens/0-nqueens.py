#!/usr/bin/python3
"""
Module 0-nqueens
A program that solves the N queens problem
"""
import sys

if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if not (num >= 4):
    print("N must be at least 4")
    sys.exit(1)


def solveNQueens(n):
    """Solution for n queens"""
    col = set()  # keep track of used columns
    pos = set()  # (r + c) keep track of used positive diagonals
    neg = set()  # (r - c) keep track of used negative diagonals

    res = []  # final result

    board = [[] for n in range(n)]  # create empy board

    def backtrack(row):
        """function for recursion"""
        # means we've reached the last row
        if row == n:
            # get copy of current solution(current board)
            copy = board.copy()
            res.append(copy)
            return

        # for every column
        for c in range(n):
            # if we find that the column or diagonals are used, then skip
            if c in col or (row + c) in pos or (row - c) in neg:
                continue

            # register found columns and diagonals
            col.add(c)
            pos.add(row + c)
            neg.add(row - c)

            board[row] = [row, c]

            # move to next row
            backtrack(row + 1)

            # finally undo
            col.remove(c)
            pos.remove(row + c)
            neg.remove(row - c)
            board[row] = []

    backtrack(0)

    return res


if __name__ == "__main__":
    boards = solveNQueens(num)
    for board in boards:
        print(board)


# #!/usr/bin/python3
# """ N queens """
# import sys


# if len(sys.argv) > 2 or len(sys.argv) < 2:
#     print("Usage: nqueens N")
#     exit(1)

# if not sys.argv[1].isdigit():
#     print("N must be a number")
#     exit(1)

# if int(sys.argv[1]) < 4:
#     print("N must be at least 4")
#     exit(1)

# n = int(sys.argv[1])


# def queens(n, i=0, a=[], b=[], c=[]):
#     """ find possible positions """
#     if i < n:
#         for j in range(n):
#             if j not in a and i + j not in b and i - j not in c:
#                 yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
#     else:
#         yield a


# def solve(n):
#     """ solve """
#     k = []
#     i = 0
#     for solution in queens(n, 0):
#         for s in solution:
#             k.append([i, s])
#             i += 1
#         print(k)
#         k = []
#         i = 0


# solve(n)
