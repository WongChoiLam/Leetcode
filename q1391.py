from typing import *
from collections import *
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        max_x = len(grid)
        max_y = len(grid[0])
        in_grid = lambda x,y : 0<=x and x<max_x and 0<=y and y<max_y
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]  # r, d, u, l
        street_directions = {1:(0,3), 2:(1, 2), 3:(1,3), 4:(0,1), 5:(2,3), 6:(0,2)}
        def path_to(x1,y1,x2,y2):
            type1 = grid[x1][y1]
            for index in street_directions[type1]:
                d = directions[index]
                nx, ny = x1 + d[0], y1 + d[1]
                if nx == x2 and ny == y2:
                    return True
            return False
        queue = deque([(0,0)])
        visited = set()
        visited.add((0,0))
        while len(queue) > 0:
            x,y = queue.popleft()
            if x==(max_x - 1) and y == (max_y - 1): return True
            street_type = grid[x][y]
            for index in street_directions[street_type]:
                d = directions[index]
                nx, ny = x + d[0], y + d[1]
                if in_grid(nx,ny) and (not (nx,ny) in visited) and path_to(nx,ny,x,y):
                    visited.add((nx,ny))
                    queue.append((nx,ny))
        return False

print(Solution().hasValidPath([[1,1,1,1,1,1,3]]))
print(Solution().hasValidPath([[1,1,2]]))