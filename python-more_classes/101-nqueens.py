#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is valid."""
    for c, r in board:
        if r == col or abs(r - col) == abs(c - row):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """Backtracking solver for N queens."""
    if row == n:
        solutions.append(list(board))
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_nqueens(n, row + 1, board, solutions)
            board.pop()


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(n, 0, [], solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
