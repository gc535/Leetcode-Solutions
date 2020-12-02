class Solution(object):
    def __init__(self):
        self.dp = []
        self.range_sum = []
        self.size = 0
        self.piles = []
    
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        self.piles = piles
        self.size = len(piles)
        self.dp = [[-1 for r in range(self.size)] for c in range(self.size)]
        self.range_sum = [[-1 for r in range(self.size)] for c in range(self.size)]
        
        self.takeOnePile(0, self.size-1)
        return (sum(self.piles) - 2*(self.dp[0][self.size-1])) < 0 
        
    
    def takeOnePile(self, begin, end):
        if (self.dp[begin][end] != -1):
            return self.getRangeSum(begin, end) - self.dp[begin][end]
        
        if (begin == end): 
            self.dp[begin][end] = self.piles[begin]
            return 0
        
        self.dp[begin][end] = max(
            (self.piles[begin] + self.takeOnePile(begin+1, end)),
            (self.piles[end] + self.takeOnePile(begin, end-1)))
        return self.getRangeSum(begin, end) - self.dp[begin][end]
    
    def getRangeSum(self, begin, end):
        if (self.range_sum[begin][end] != -1): return self.range_sum[begin][end]
        
        self.range_sum[begin][end] = sum(self.piles[begin:end+1])
        return self.range_sum[begin][end]