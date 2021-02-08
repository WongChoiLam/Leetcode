from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_rotten = 0
        total_orange = 0
        queue = []
        visited = set()
        total_steps = -1
        for i,row in enumerate(grid):
            for j,orange in enumerate(row):
                if orange == 2:
                    total_rotten += 1
                    queue.append((0, (i,j)))
                    visited.add((i,j))
                if orange != 0:
                    total_orange += 1
        if total_rotten == total_orange: return 0
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]
        max_x = len(grid)
        max_y = len(grid[0])
        while len(queue) > 0 :
            step, coord = queue.pop(0)
            total_steps = step
            x, y = coord
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx and nx < max_x and 0 <= ny and ny < max_y and (not (nx,ny) in visited) and grid[nx][ny] == 1:
                    queue.append((step + 1, (nx,ny)))
                    visited.add((nx,ny))
        if len(visited) == total_orange:
            return total_steps
        return -1
grid = [[2,1,1],[0,1,1],[1,0,1]]
print(Solution().orangesRotting(grid))

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))