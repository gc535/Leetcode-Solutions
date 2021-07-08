class Solution(object):
    def pacificAtlantic(self, heights):
        rows = len(heights) 
        cols = len(heights[0])
        if rows <= 1: return [[0, c] for c in range(cols)]
        if cols <= 1: return [[r, 0] for r in range(rows)]

        def checkInBound(r, c):
            return r >= 0 and c >= 0 and r < rows and c < cols

        def dfs(r, c, val, record, check):
            if not checkInBound(r, c): return -1

            cur_val = heights[r][c]
            if cur_val > val: return -1
                
            if record[r][c] != 0: return record[r][c]
            if check[r][c]: return -1
            
            check[r][c] = 1
            if dfs(r, c-1, cur_val, record, check) > 0 or dfs(r, c+1, cur_val, record, check) > 0 or \
                dfs(r-1, c, cur_val, record, check) > 0 or dfs(r+1, c, cur_val, record, check) > 0:
                check[r][c] = 0
                record[r][c] = 1
                return True
            check[r][c] = 0
            return False

        paciRecord = [[0 for c in range(cols)] for r in range(rows)]
        atlaRecord = [[0 for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            paciRecord[r][0] = 1
            atlaRecord[r][cols-1] = 1

        for c in range(cols):
            paciRecord[0][c] = 1
            atlaRecord[rows-1][c] = 1
        
        check1 = [[0 for x in range(cols)] for y in range(rows)]
        check2 = [[0 for x in range(cols)] for y in range(rows)]
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, heights[r][c], paciRecord, check1)
                check1[r][c] = 1
                dfs(rows-1-r, cols-1-c, heights[rows-1-r][cols-1-c], atlaRecord, check2)
                check2[rows-1-r][cols-1-c] = 1
        
        ret = list()
        for r in range(rows):
            for c in range(cols):
                if paciRecord[r][c] > 0 and atlaRecord[r][c] > 0:
                    ret.append([r, c])
        return ret

