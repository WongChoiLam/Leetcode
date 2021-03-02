from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        max_y = len(board)
        max_x = len(board[0])
        inbound = lambda y,x : -1 < y and y < max_y and -1 < x and x < max_x
        directions = [(0,1), (1,0), (0,-1),(-1,0)]
        stack = []
        for y in range(max_y):
            for x in range(max_x):
                if board[y][x] == word[0]:
                    stack.append([(y,x)])
        while len(stack) > 0:
            ans = stack.pop()
            y,x = ans[-1]
            if len(ans) == len(word): return True
            for d in directions:
                ny, nx = y+d[0], x+d[1]
                if inbound(ny,nx) and word[len(ans)] == board[ny][nx] and not (ny,nx) in ans:
                    stack.append(ans + [(ny,nx)])
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

s = Solution()
print(s.exist(board, word))