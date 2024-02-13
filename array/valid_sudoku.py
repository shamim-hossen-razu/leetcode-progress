from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = []
        for row in board:
            rows = []
            for col in row:
                if col == '.':
                    rows.append(0)
                else:
                    rows.append(int(col))
            sudoku.append(rows)

        
        # check rows            
        for row in sudoku:
            check = []
            for value in row:
                if value != 0 and value in check:
                    return False
                else:
                    check.append(value)
                    
        # check cols
        for col in range (0,9):
            check = []
            for row in range(0, 9):
                if sudoku[row][col] != 0 and sudoku[row][col] in check:
                    return False
                else:
                    check.append(sudoku[row][col])
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                max_row = i+ 2
                max_col = j + 2
                check = []
                for k in range(i, max_row+1):
                    for l in range(j, max_col+1):
                        if sudoku[k][l] != 0 and sudoku[k][l] in check:
                            return False
                        else:
                            check.append(sudoku[k][l])
                
        return True

print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."]
                                ,["6",".",".","1","9","5",".",".","."]
                                ,[".","9","8",".",".",".",".","6","."]
                                ,["8",".",".",".","6",".",".",".","3"]
                                ,["4",".",".","8",".","3",".",".","1"]
                                ,["7",".",".",".","2",".",".",".","6"]
                                ,[".","6",".",".",".",".","2","8","."]
                                ,[".",".",".","4","1","9",".",".","5"]
                                ,[".",".",".",".","8",".",".","7","9"]]))

        