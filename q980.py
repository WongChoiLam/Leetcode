from typing import List
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def in_grid(y,x):
            return -1 < y and y < len(grid) and -1 < x and x < len(grid[0])
        init_y, init_x = 0,0
        obstacle_num = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == -1:
                    obstacle_num += 1
                elif grid[y][x] == 1:
                    init_y, init_x = y,x
        non_obstacle_num = len(grid) * len(grid[0]) - obstacle_num
        def bt(y,x):
            bt.visited.append((y,x))
            if grid[y][x] == 2 and len(bt.visited) == non_obstacle_num:
                bt.ans += 1
                return
            old_len = len(bt.visited)
            for d in directions:
                ny,nx = y + d[0], x + d[1]
                if in_grid(ny,nx) and (not (ny,nx) in bt.visited) and grid[ny][nx] != -1:
                    bt(ny,nx)
                    bt.visited = bt.visited[:old_len]
        bt.ans = 0
        bt.visited = []
        bt(init_y, init_x)
        return bt.ans
        