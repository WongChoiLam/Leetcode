from typing import List
from collections import *
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        max_x = len(grid)
        max_y = len(grid[0])
        in_grid = lambda x,y : 0<=x and x<max_x and 0<=y and y<max_y
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]  # r, d, u, l
        queue = deque()
        visited = set()
        total_block = max_x * max_y
        total_land = 0
        
        for i in range(max_x):
            for j in range(max_y):
                if grid[i][j] == 1:
                    total_land += 1
                    queue.append((0, (i,j)))
                    visited.add(i * max_y + j)
        if total_land == 0 or total_land == total_block:
            return -1
        
        max_step = 0
        while len(queue) > 0:
            step, (x,y) = queue.popleft()
            max_step = max(max_step, step)
            for d in directions:
                nx,ny = x+d[0],y+d[1]
                if in_grid(nx,ny) and grid[nx][ny] == 0 and (not (nx * max_y + ny) in visited):
                    visited.add((nx * max_y + ny))
                    queue.append((step+1,(nx,ny)))
        return max_step

print(Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]]))