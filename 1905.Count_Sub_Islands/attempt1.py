class Solution(object):
    def countSubIslands(self, grid1, grid2):
        rows = len(grid1)
        cols = len(grid1[0])
        
        def markIsland(grid, x, y, marker, marked):
            if x < 0 or y < 0 or x >= rows or y >= cols: return False 
            if grid[x][y] == 0: return False 
            if marked[x][y] != -1: return False
            
            
            marked[x][y] = marker
            markIsland(grid, x, y-1, marker, marked)
            markIsland(grid, x, y+1, marker, marked)
            markIsland(grid, x-1, y, marker, marked)
            markIsland(grid, x+1, y, marker, marked)
            
            return True
        
        marker1 = marker2 = 1
        marked1 = [[-1 for c in range(cols)] for r in range(rows)]
        marked2 = [[-1 for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                marker1 += (1 if markIsland(grid1, r, c, marker1, marked1) else 0)
                marker2 += (1 if markIsland(grid2, r, c, marker2, marked2) else 0)

            
        counted = dict()
        ignored = set()
        for r in range(rows):
            for c in range(cols):
                if marked2[r][c] != -1 and marked2[r][c] not in ignored:
                    if marked1[r][c] == -1: 
                        counted.pop(marked2[r][c], None)
                        ignored.add(marked2[r][c])
                        continue
                        
                    if marked2[r][c] not in counted:
                        counted[marked2[r][c]] = marked1[r][c]
                    elif counted[marked2[r][c]] != marked1[r][c]:
                        counted.pop(marked2[r][c], None)
                        ignored.add(marked2[r][c])
        
        return len(counted)
                        
                    
        
