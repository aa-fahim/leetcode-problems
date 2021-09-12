'''
  DFS Approach
  
  Time Complexity: O((n * m)^ 2) where n is the number of rows and m is the number of columns in the matrix.
  
  Iterate through each position of the grid and perform DFS until we have visited a node that touches the atlantic ocean and a node that touches the pacific ocean.
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        
        def dfs(r, c):
            pacific = False
            atlantic = False
            stack = [(r,c)]
            moves = [(0,1), (0,-1), (1,0), (-1,0)]
            visited = set()
            
            while(len(stack) > 0):
                r, c = stack.pop(-1)
                visited.add((r,c))
                if r == 0 or c == 0:
                    pacific = True
                if r == rows - 1 or c == cols - 1:
                    atlantic = True
                if atlantic and pacific:
                    break
                
                for nr, nc in moves:
                    if (r + nr, c + nc) not in visited and (r + nr) in range(rows) and (c + nc) in range(cols) and heights[r][c] >= heights[r + nr][c + nc]:
                        stack.append((r + nr, c + nc))
                    
            return pacific and atlantic
        
        for r in range(rows):
            for c in range(cols):
                tmp = dfs(r, c)
                if tmp == True:
                    res.append([r, c])
                
        return res
        
