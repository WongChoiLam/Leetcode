from typing import List
class Solution:
    def validAt(self, board : List[List[str]], location : (int, int)):
        r, c = location
        # check row
        row = [board[r][c] for c in range(9)]
        row = list(filter(lambda x : x!='.', row))
        if len(row) != len(set(row)): return False
        # check column
        column = [board[r][c] for r in range(9)]
        column = list(filter(lambda x : x!='.', column))
        if len(column) != len(set(column)): return False
        # check block
        R, C = int(r / 3), int(c / 3)
        block = []
        for r in range(3):
            for c in range(3):
                num = board[R*3 + r][C*3 + c]
                if num == '.': continue
                if num in block: return False
                block.append(num)
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        empty = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    empty.append((i, j))
        def fill(answer):
            for i,c in enumerate(empty):
                y,x = c
                if i < len(answer):
                    board[y][x] = answer[i]
                else:
                    board[y][x] = '.'
        stack = [[]]
        while len(stack) > 0:
            answer = stack.pop()
            if len(answer) == len(empty):
                fill(answer)
                return
            for i in range(1,10):
                next_answer = answer + [str(i)]
                fill(next_answer)
                if not self.validAt(board, empty[len(next_answer) - 1]): continue
                stack.append(next_answer)
board = \
[["5","3",".",".","7",".",".",".","."],\
["6",".",".","1","9","5",".",".","."],\
[".","9","8",".",".",".",".","6","."],\
["8",".",".",".","6",".",".",".","3"],\
["4",".",".","8",".","3",".",".","1"],\
["7",".",".",".","2",".",".",".","6"],\
[".","6",".",".",".",".","2","8","."],\
[".",".",".","4","1","9",".",".","5"],\
[".",".",".",".","8",".",".","7","9"]]

Solution().solveSudoku(board)
for line in board:
    print(line)

print()

board = \
[[".",".",".","2",".",".",".","6","3"],\
["3",".",".",".",".","5","4",".","1"],\
[".",".","1",".",".","3","9","8","."],\
[".",".",".",".",".",".",".","9","."],\
[".",".",".","5","3","8",".",".","."],\
[".","3",".",".",".",".",".",".","."],\
[".","2","6","3",".",".","5",".","."],\
["5",".","3","7",".",".",".",".","8"],\
["4","7",".",".",".","1",".",".","."]]

Solution().solveSudoku(board)
for line in board:
    print(line)