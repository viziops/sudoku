from sudoku import Sudoku
# Initializes a Sudoku puzzle with 3 x 3 sub-grid and
# generates a puzzle with half of the cells empty
puzzle = Sudoku(3).difficulty(0.8)
puzzle.show()


solution = puzzle.solve()
solution.show()


solution.board
# [[4, 1, 5, 3, 8, 9, 7, 6, 2],
#  [8, 9, 3, 6, 7, 2, 4, 5, 1],
#  [2, 6, 7, 1, 4, 5, 9, 8, 3],
#  [9, 5, 8, 4, 1, 6, 2, 3, 7],
#  [3, 4, 6, 5, 2, 7, 8, 1, 9],
#  [1, 7, 2, 8, 9, 3, 5, 4, 6],
#  [5, 8, 9, 2, 6, 1, 3, 7, 4],
#  [6, 2, 4, 7, 3, 8, 1, 9, 5],
#  [7, 3, 1, 9, 5, 4, 6, 2, 8]]

solution.width
# 3

solution.height
# 3