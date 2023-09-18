# Difficulty: 3 kyu

def sudoku(puzzle):
    def is_valid_move(puzzle, x, y, num):
        # Check if num is in the same row or column
        for i in range(9):
            if puzzle[x][i] == num or puzzle[i][y] == num:
                return False
        
        # Check if num is in the same 3x3 grid
        grid_x, grid_y = x // 3 * 3, y // 3 * 3
        for i in range(3):
            for j in range(3):
                if puzzle[grid_x + i][grid_y + j] == num:
                    return False
        return True

    def solve(puzzle):
        for x in range(9):
            for y in range(9):
                if puzzle[x][y] == 0:
                    for num in range(1, 10):
                        if is_valid_move(puzzle, x, y, num):
                            puzzle[x][y] = num
                            if solve(puzzle):
                                return True
                            else:
                                puzzle[x][y] = 0
                    return False
        return True

    solve(puzzle)
    return puzzle

puzzle = [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]

print(sudoku(puzzle))