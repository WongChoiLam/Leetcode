class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for r in range(9):
            row = [board[r][c] for c in range(9)]
            row = list(filter(lambda x : x!='.', row))
            if len(row) != len(set(row)): return False
        # check column
        for c in range(9):
            column = [board[r][c] for r in range(9)]
            column = list(filter(lambda x : x!='.', column))
            if len(column) != len(set(column)): return False
        # check block
        for R in range(3):
            for C in range(3):
                block = []
                for r in range(3):
                    for c in range(3):
                        num = board[R*3 + r][C*3 + c]
                        if num == '.': continue
                        if num in block: return False
                        block.append(num)
        return True