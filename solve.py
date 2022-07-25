puzzle = [
        [3, 9, 0,  0, 5, 0,  0, 0, 0],
        [0, 0, 0,  2, 0, 0,  0, 0, 5],
        [0, 0, 0,  7, 1, 9,  0, 8, 0],

        [0, 5, 0,  0, 6, 8,  0, 0, 0],
        [2, 0, 6,  0, 0, 3,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 4],

        [5, 0, 0,  0, 0, 0,  0, 0, 0],
        [6, 7, 0,  0, 0, 5,  0, 4, 0],
        [0, 0, 9,  0, 0, 0,  2, 0, 0]
    ]

copy = [
        [3, 9, 0,  0, 5, 0,  0, 0, 0],
        [0, 0, 0,  2, 0, 0,  0, 0, 5],
        [0, 0, 0,  7, 1, 9,  0, 8, 0],

        [0, 5, 0,  0, 6, 8,  0, 0, 0],
        [2, 0, 6,  0, 0, 3,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 4],

        [5, 0, 0,  0, 0, 0,  0, 0, 0],
        [6, 7, 0,  0, 0, 5,  0, 4, 0],
        [0, 0, 9,  0, 0, 0,  2, 0, 0]
    ]


def get_empty(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return None, None


def is_valid(sudoku, num, row, col):
    # checking for rows
    for i in range(9):
        if sudoku[row][i] == num:
            return False

    # checking for cols
    for i in range(9):
        if sudoku[i][col] == num:
            return False

    # checking for box
    block = ((row // 3) * 3, (col // 3) * 3)
    for i in range(block[0], block[0] + 3):
        for j in range(block[1], block[1] + 3):
            if sudoku[i][j] == num:
                return False

    return True


def solve(sudoku):
    row, col = get_empty(sudoku)

    if row is None:
        return True

    for num in range(1, 10):
        if is_valid(sudoku, num, row, col):
            sudoku[row][col] = num

            if solve(sudoku):
                return True
        sudoku[row][col] = 0

    return False


if __name__ == '__main__':
    print(solve(puzzle))
    print(puzzle)
