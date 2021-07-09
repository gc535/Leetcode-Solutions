class Solution(object):
    def findPeakGrid(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        left = 0
        right = cols - 1
        
        def getMaxPos(l, r, mat):
            maxVal = -1
            for y in range(l, r+1):
                for x in range(rows):
                    if mat[x][y] > maxVal:
                        maxVal = mat[x][y]
                        ret = [x, y]
            return ret
                
        while left + 1 < right:
            mid = (left + right)/2
            [x, y] = getMaxPos(mid-1, mid+1, mat)
            if y == mid: return [x, y]
            elif y < mid: right = y
            else: left = y        
            
        return getMaxPos(left, right, mat)    
        
