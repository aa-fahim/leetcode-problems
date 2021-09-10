'''
  Time Complexity: O(2*n * 2*m) where n is the number of rows and m is the number of columns in the 2D array.
  
  Traverse through each position of the grid and perform breadth-first search on the position if it has not been already visited and is marked '1' indicating it
  is land. The breadth-first search assumes we can move to the right, left, up or down. We evaluate all these moves to the current position if the new position does
  not go out of bounds of the grid, has not been already visited and is land.
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r,c):
            visited.add((r,c))
            queue = [(r,c)]
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while (len(queue) > 0):
                r,c = queue.pop(0)
                for nr, nc in moves:
                    row = r + nr
                    col = c + nc
                    if row > -1 and row < rows and col > -1 and col < cols and grid[row][col] == '1' and (row,col) not in visited:
                        queue.append((row, col))
                        visited.add((row, col))
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    islands += 1
                    bfs(r,c)
        return islands
