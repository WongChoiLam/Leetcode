from typing import List
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        max_y = len(grid)
        max_x = len(grid[0])
        
        in_grid = lambda y,x: 0<=y and y<max_y and 0<=x and x<max_x
        on_edge = lambda y,x: y==0 or x==0 or y==(max_y-1) or x==(max_x-1)
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        visited = set()
        
        def dfs(sy,sx):
            flag = True
            stack = [(sy,sx)]
            visited.add((sy,sx))
            while len(stack) > 0:
                y,x = stack.pop()
                if on_edge(y,x): flag = False
                for d in directions:
                    ny,nx = y+d[0], x+d[1]
                    if in_grid(ny,nx) and (not (ny,nx) in visited) and grid[ny][nx] == 0:
                        stack.append((ny,nx))
                        visited.add((ny,nx))
            return flag
        ans = 0
        for y in range(max_y):
            for x in range(max_x):
                if grid[y][x] == 1 or (y,x) in visited: continue
                # print("dfs",y,x)
                if dfs(y,x):
                    ans+=1
                    # print("Found island")
        return ans

a =[[0,0,1,1,0,1,0,0,1,0],
    [1,1,0,1,1,0,1,1,1,0],
    [1,0,1,1,1,0,0,1,1,0],
    [0,1,1,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,1,1,1,0],
    [0,1,0,1,0,1,0,1,1,1],
    [1,0,1,0,1,1,0,0,0,1],
    [1,1,1,1,1,1,0,0,0,0],
    [1,1,1,0,0,1,0,1,0,1],
    [1,1,1,0,1,1,0,1,1,0]]

print(Solution().closedIsland(a))