class Solution(object):
    def __init__(self):
        self.ans = set()
        self.n = 0
        self.seen = set()
    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 0: return []
        
        self.n = n
        arrange = [["." for c in range(n)] for r in range(n)]
        spots = []
        for r in range(n):
            for c in range(n):
                spots.append([r, c])
        self.fillNext(n, spots, arrange)
        return self.getAns()
        
        
    def fillNext(self, remain, spots, arrange):
        # skip seen scenarios for optimization
        key = self.genArrangeKey(arrange)
        if key in self.seen:
            return 
        self.seen.add(key)
        
        # no solution
        if len(spots) < remain: return 
        
        # found a solution
        if remain == 1 and len(spots) >= 1:
            for [r, c] in spots: 
                arrange[r][c] = "Q"
                self.ans.add( self.genArrangeKey(arrange) )
                arrange[r][c] = "."
                
        # go fill next queen
        while spots:
            [r, c] = spots.pop(0)
            arrange[r][c] = "Q"
            new_spots = self.filter_spots(r, c, spots)
            self.fillNext(remain-1, new_spots, arrange)
            arrange[r][c] = "."
    
    def filter_spots(self, x, y, spots):
        ret = []
        for [r, c] in spots:
            skip = False
            if r == x or c == y: skip = True
            elif r-x == c-y or r-x == y-c: skip = True
            elif x-r == c-y or x-r == y-c: skip = True
            if skip == False: ret.append([r, c])
        return ret
            
            
    def getAns(self):
        ret = []
        for val in self.ans:
            ret.append([val[i:i+self.n] for i in range(0, len(val), self.n)])
        return ret

    def genArrangeKey(self, arrange):
        return "".join( ["".join(row) for row in arrange] )