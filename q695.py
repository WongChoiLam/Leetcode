class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_y = len(grid)
        max_x = len(grid[0])
        
        in_grid = lambda y,x: 0<=y and y<max_y and 0<=x and x<max_x
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        visited = set()
        
        def dfs(sy,sx):
            area = 0
            stack = [(sy,sx)]
            visited.add((sy,sx))
            while len(stack) > 0:
                area += 1
                y,x = stack.pop()
                for d in directions:
                    ny,nx = y+d[0], x+d[1]
                    if in_grid(ny,nx) and (not (ny,nx) in visited) and grid[ny][nx] == 1:
                        stack.append((ny,nx))
                        visited.add((ny,nx))
            return area
        ans = 0
        for y in range(max_y):
            for x in range(max_x):
                if grid[y][x] == 0 or (y,x) in visited: continue
                ans = max(dfs(y,x), ans)
        return ans